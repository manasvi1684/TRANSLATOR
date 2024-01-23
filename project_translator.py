from dotenv import load_dotenv
load_dotenv()  # Load environment variable
import os
import google.generativeai as genai
import streamlit as st
from translate import Translator

# Input
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])  # Chat initialization
with st.sidebar:
    st.write('Contents-\nsettings\n')
# Initialize the translator with the 'MyMemory' API key
  # Set default translation direction

def translate_text(text, target_language):
    try:
        translated_text = translator.translate(text)  # Pass only two arguments
        return translated_text
    except Exception as e:
        st.write(f"Error: {e}")
        return None

st.title("Language Translator")
# if 'chat_history' not in st.session_state:  # Session state is like cache memory
#     st.session_state['chat_history'] = []

input_text = st.text_input("Enter text to translate:")

target_language = st.selectbox("Target Language", ["Spanish", "French", "German", "Chinese", "Japanese", "Korean", "Telegu", "Tamil", "Marathi", "Bengali","Hindi"])
input_prompt="""You are an expert in translating languages with english alphabets.We will input our sentences,phrases and words in english or hindi and you will have to ansewer the question by translating it into the target languages with english spelling of the translation."""
translator = Translator(to_lang=target_language, from_lang="EN")
submit = st.button("Translate")

if input_text and submit:
    value = translate_text(input_text, target_language)  # Attempt translation
    if value:
       st.write(f"Translated Text: {value}")  # Display translation if successful
    else:
       st.write("Error occurred during translation.")  # Handle translation failure
