import streamlit as st

st.set_page_config(page_title="Aditya AI Guruji", page_icon="🎓")
st.title("🎓 Aditya AI Guruji")
st.subheader("BSc CS Students ki AI Doubt Solver - by Sai Durga")

doubt = st.text_input("Nee Doubt Enti? (Ex: pointer, dbms, stack)")

if st.button("Ask Guruji"):
    if "pointer" in doubt.lower():
        st.success("Pointer ante variable address ni store chese variable. Ex: int *p = &a;")
    elif "dbms" in doubt.lower():
        st.success("DBMS ante Database Management System. Data ni store, manage cheyadaniki use chestham.")
    elif "stack" in doubt.lower():
        st.success("Stack ante LIFO - Last In First Out. Ex: Plates stack.")
    elif doubt == "":
        st.warning("Doubt type cheyyi Sai Durga!")
    else:
        st.info(f"'{doubt}' gurinchi Guruji alochistunnadu... Soon answer add chestham!")
