import streamlit as st
import json
import random

st.logo("ic.png")
st.sidebar.header("Himakino by Hirafuyu")
st.sidebar.image("ic.png")
st.sidebar.write("Hi! my name is Himakino, i'm a chatbot developped by Hirafuyu to simulate her character! hope you like talking me...")
if st.sidebar.button("Contact Us"):
    st.write("Contacting Hirafuyu!")

# Load your JSON data
with open('knowledge.json', 'r') as f:
    data = json.load(f)

# Function to find the best matching answer
def get_answer(user_input):
    user_input = user_input.lower()
    for question in data["questions"]:
        if user_input == question["question"].lower():
            if isinstance(question["answer"], list):
                return random.choice(question["answer"])
            else:
                return question["answer"]
    return "I don't understand. Can you rephrase?"

# Streamlit UI
st.header("Welcome to HiraBot Land!!")
st.title("Hi! How are you doing?")

# Display chat history
st.text("Start chat:")

# Get the session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input field
user_input = st.chat_input("You:")

# Process user input and generate response
if user_input:
    response = get_answer(user_input)
    st.session_state.chat_history.append(f"You: {user_input}")
    st.session_state.chat_history.append(f"Himakino: {response}")

    for message in st.session_state.chat_history:
        st.text(message)

    # Display the chatbot's response
    # st.text(response)
    if response == "I don't understand. Can you rephrase?":
        st.sidebar.success("Hira's Notified, will answer in future! :heart:")
# Optional: Add a button to clear chat history
if st.button("Clear Chat"):
    with open("Upgrade.txt", "a") as f: # Open in append mode
                f.write(f"{st.session_state.chat_history}\n") 
    st.session_state.chat_history.clear()
