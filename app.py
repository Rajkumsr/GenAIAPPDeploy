import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
# Load environment variables from .env file (if it exists)
load_dotenv()

# Title of the web app
st.title("My GenAI Application 🚀")
st.write("This app uses Groq for blazing-fast text generation.")

# Securely retrieve the API key
# This checks Streamlit's secrets manager first, then environment variables
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API Key is missing. Please set GROQ_API_KEY in your deployment secrets.")
    st.stop()

# Initialize the Groq client
client = Groq(api_key=api_key)

# User input
user_input = st.text_input("Enter a prompt:")

if st.button("Generate"):
    if user_input:
        with st.spinner("Generating response via Groq..."):
            try:
                # Make the API call to Groq
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": user_input,
                        }
                    ],
                    # Using LLaMA 3 8B, but you can swap this for 'mixtral-8x7b-32768'
                    model="llama-3.3-70b-versatile", 
                    max_tokens=150,
                )
                
                st.success("Done!")
                # Display the generated text
                st.write(chat_completion.choices[0].message.content)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt first.")
