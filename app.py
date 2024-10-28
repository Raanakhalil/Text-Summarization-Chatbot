import streamlit as st
from transformers import pipeline

# Load the summarization pipeline globally
@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

st.title("Text Summarization Tool")

# Text input from the user
user_input = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if user_input:
        summary = summarize_text(user_input)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize!")

