# streamlit_app.py
import streamlit as st
import requests

st.title("AgenticRAG")

token = st.text_input("JWT Token")
question = st.text_input("Question")

if st.button("Ask"):
    res = requests.post(
        "http://localhost:8000/ask",
        params={"question": question},
        headers={"Authorization": f"Bearer {token}"}
    )
    if res.status_code == 200:
        try:
            data = res.json()
            st.write(data["answer"])
        except:
            st.write(res.text)
    else:
        st.error(res.text)

