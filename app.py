import streamlit as st
from transformers import pipeline

# Title of the web app
st.title("My GenAI Application")
st.write("This is a simple Generative AI app deployed on the cloud.")

# Load a lightweight open-source text generation model
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# User input
user_input = st.text_input("Enter a prompt:")

if st.button("Generate"):
    if user_input:
        with st.spinner("Generating response..."):
            response = generator(user_input, max_length=50, num_return_sequences=1)
            st.success("Done!")
            st.write(response[0]['generated_text'])
    else:
        st.warning("Please enter a prompt first.")