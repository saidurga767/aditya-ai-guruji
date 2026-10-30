import streamlit as st
from google import genai

# Secrets nundi key
API_KEY = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=API_KEY)

st.set_page_config(page_title="Aditya AI Guruji")
st.title("Aditya AI Guruji 🤖")
st.write("BSc Computer Science Doubt Solver - by Sai Durga")

question = st.text_input("Nee Doubt Adugu:")

if st.button("Ask Guruji 🔥"):
    if question:
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=question
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Question type cheyyi Durga!")
