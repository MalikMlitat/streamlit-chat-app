import streamlit as st


def generate_response(message: str) -> str:
    reversed_msg = message[::-1]
    return f"You said: '{message}'. Here's my take: {reversed_msg}"


st.title("💬 Chat App")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "tell me what do you need..."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
