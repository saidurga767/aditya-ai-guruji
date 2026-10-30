import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Aditya AI Guruji")
st.title("📚 Aditya AI Guruji")
st.write("BSc Computer Science Doubt Solver - by Sai Durga")

# NEE KEY IKKADA PASTE CHEYYI - quotes lopala
API_KEY = "PASTE YOUR GEMINI KEY HERE"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

doubt = st.text_input("Nee Doubt Adugu (Ex: What is array?)")

if st.button("Ask Guruji 🔥"):
    if doubt:
        with st.spinner("Guruji alochistunnadu..."):
            prompt = f"You are Aditya AI Guruji, friendly teacher for BSc CS students. Explain '{doubt}' in simple Telugu + English mix with example."
            response = model.generate_content(prompt)
            st.success(response.text)
    else:
        st.warning("Doubt type cheyyi Durga!")
