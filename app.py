import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

st.title("Text Summarization Tool")

# Text input from the user
user_input = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if user_input:
        summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize!")
