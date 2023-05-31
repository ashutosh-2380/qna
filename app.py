import streamlit as st
from transformers import pipeline

# Load the question answering model
model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Set up the Streamlit app
st.title("Question Answering App")

# Input fields for the user to enter question and context
question = st.text_input("Enter your question:")
context = st.text_area("Enter the context:")

# Generate the answer when the user clicks the "Answer" button
if st.button("Answer"):
    # Perform question answering
    answer = model(question=question, context=context)

    # Display the answer
    st.write("Answer:", answer["answer"])
    st.write("Confidence score:", answer["score"])
