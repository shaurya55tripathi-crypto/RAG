"""Streamlit chat app for the HR Policy Assisstant.

Run with : streamlit run app.py
"""

import streamlit as st

from hr_assisstant.pipeline import ask, build_hr_assistant

st.set_page_config(page_title="HR Policy Assisstant", page_icon="🤖")
st.title("🤖 HR Policy Assisstant")
st.caption("Ask me anything abouth the company HR policy documents.")

@st.cache_resource(show_spinner='Setting up the assisstant (only happens once)...')
def get_agent():
    return build_hr_assistant()

agent = get_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Get a new question from the user
question = st.chat_input("Ask a question about HR policy...")

if question:
    st.session_state.messages.append({"role":"user", "content":question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assisstant"):
        with st.spinner("Thinking..."):
            answer = ask(agent, question)
        st.markdown(answer)
    st.session_state.messages.append({"role":"assisstant", "content":answer})
