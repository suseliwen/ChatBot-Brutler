import streamlit as st
from chatbot import BruttlerBot


def init_session_states():
    # initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "bot" not in st.session_state:
        st.session_state.bot = BruttlerBot()


def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_input():

    if prompt := st.chat_input("What can this lowly Buttler help you with M'lord/Madam?"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_state.bot.chat(prompt).get("bot")

        response = f": {bot_response}"

        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


def layout():
    st.markdown("# Command your Bruttler Bot")
    st.write(
        "Bruttler Bot is a posh British butler who always answers politely and uses titles.")

    display_chat_messages()
    handle_user_input()

    #tester


if __name__ == "__main__":
    init_session_states()
    layout()

    