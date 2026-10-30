import streamlit as st
from google import genai

st.set_page_config(page_title="Aditya AI Guruji", page_icon="🤖", layout="wide")

API_KEY = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=API_KEY)

# --- BLUE PURPLE GRADIENT HEADER - NO BUBBLE ISSUE ---
st.markdown("""
<style>
    .header-box {
        background: linear-gradient(90deg, #7c3aed 0%, #6366f1 50%, #3b82f6 100%);
        padding: 20px 25px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 8px 20px rgba(124, 58, 237, 0.3);
        margin-bottom: 20px;
    }
    .stChatMessage { border-radius: 15px; }
</style>
<div class="header-box">
    <h2 style='margin:0; color:white;'>🎓 Aditya AI Guruji</h2>
    <p style='margin:5px 0 0 0; opacity:0.95;'>BSc Computer Science • Doubt Solver • by Sai Durga 👩‍💻</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2.5])

with col1:
    st.markdown("#### 📚 Subjects")
    subject = st.radio("Select", ["C", "Java", "DBMS", "OS", "DS", "CN"], label_visibility="collapsed")
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #ede9fe, #dbeafe); padding:12px; border-radius:10px; border-left: 4px solid #7c3aed;'>
        <b>Selected:</b> {subject}<br>
        <small>Ready to help!</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 🕒 Recent")
    st.caption("• What is recursion?")
    st.caption("• Pointers in C")
    st.caption("• Normalization DBMS")
    st.success("🎓 BSc CS Final Year")

with col2:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": f"Hi Sai Durga! 👋 Nenu **Aditya AI Guruji**! \n\n **{subject}** lo edaina doubt adugu, instant ga explain chestha with example! 💙"}
        ]

    # Chat container with white background
    with st.container(border=True):
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])

    # Input
    if prompt := st.chat_input(f"Ask doubt in {subject}..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.container(border=True):
            for m in st.session_state.messages[-2:]:
                with st.chat_message(m["role"]):
                    st.markdown(m["content"])
        
        with st.chat_message("assistant"):
            with st.spinner("💭 Guruji thinking..."):
                q = f"You are Aditya AI Guruji, friendly BSc {subject} teacher. Explain simply with code example. Doubt: {prompt}"
                res = client.models.generate_content(model="gemini-3.5-flash-lite", contents=q)
                st.markdown(res.text)
                st.session_state.messages.append({"role": "assistant", "content": res.text})
        st.rerun()

st.markdown("<p style='text-align:center; color: #7c3aed; font-size:13px; margin-top:15px;'>Made with 💙💜 by Sai Durga | Aditya Degree College</p>", unsafe_allow_html=True)
