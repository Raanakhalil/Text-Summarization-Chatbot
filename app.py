import streamlit as st
from transformers import pipeline

# Load the summarization pipeline globally and cache it
@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

def summarize_text(text):
    # Truncate text if it exceeds 1024 characters (approximately)
    max_length = 1024
    if len(text) > max_length:
        text = text[:max_length]

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Streamlit UI
st.title("Text Summarization Tool")

# Text input from the user
user_input = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if user_input:
        summary = summarize_text(user_input)  # Call the summarize_text function
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize!")


