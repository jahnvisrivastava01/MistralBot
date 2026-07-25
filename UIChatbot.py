import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.title("AI Chatbot")
st.markdown("### 👋 Welcome!")
st.caption("Choose an AI personality and start chatting below.")

model = ChatMistralAI(
    model="mistral-small-latest"
)

st.subheader("choose your AI mode")
choice = st.radio(
    "select mode",
    ["1 - Angry Mode", "2 - Funny Mode", "3 - Normal Mode"]
)

if choice.startswith("1"):
    mode = "You are an angry AI Agent. You respond aggresively and impatiently"
elif choice.startswith("2"):
    mode = "You are a funny AI Agent. You respond with humor and jokes"
elif choice.startswith("3"):
    mode = "You are a normal AI Agent. You have answers to all the questions."

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

if "mode" not in st.session_state or st.session_state.mode != mode:
    st.session_state.mode = mode
    st.session_state.messages = [SystemMessage(content=mode)]



for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("You:")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content) 

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Made by <b>Jahnvi Srivastava</b></p>",
    unsafe_allow_html=True
)