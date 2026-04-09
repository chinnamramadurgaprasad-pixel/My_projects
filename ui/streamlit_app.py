import streamlit as st
import requests

# Django backend URL
BASE_URL = "http://127.0.0.1:8000/api"

st.set_page_config(page_title="Multi-Agent Assistant", layout="wide")

st.title(" Multi-Agent Research Assistant")

# INPUT SECTION

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        with st.spinner("Agents are thinking..."):
            try:
                response = requests.post(
                    f"{BASE_URL}/ask/",
                    json={"question": question}
                )

                if response.status_code == 200:
                    data = response.json()

                    st.success("Answer generated!")
                    st.write("### Answer")
                    st.write(data["answer"])

                else:
                    st.error("Error from backend")

            except Exception as e:
                st.error(f"Connection error: {e}")

# HISTORY SECTION
st.markdown("---")
st.subheader("Conversation History")

if st.button("Load History"):
    try:
        response = requests.get(f"{BASE_URL}/conversations/")

        if response.status_code == 200:
            conversations = response.json()

            for convo in conversations:
                with st.expander(f"Q: {convo['question']}"):
                    st.write("**Answer:**", convo["answer"])
                    st.write("**ID:**", convo["id"])

        else:
            st.error("Failed to fetch history")

    except Exception as e:
        st.error(f"Error: {e}")