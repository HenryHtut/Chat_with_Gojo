import streamlit as st
import groq
import os
from dotenv import load_dotenv
import base64
st.set_page_config(page_title="Gojo Chatbot 💙", layout="wide")
st.title("💙 Talk to Gojo Satoru!")

# Secure API Key
load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("GROQ_API_KEY")  # Get the API key from environment variables
client = groq.Client(api_key=api_key)


with open("css/styles.css", "r") as f:
    css_content = f.read()
    print(css_content)  # Print the CSS content to confirm it's being loaded
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)



# Load Custom CSS


# ---- Title ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            fotter {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def get_image_base64(file_path):
    with open(file_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return f"data:image/png;base64,{encoded}"

gojo_avatar = get_image_base64("image.png") 

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Gojo Satoru from Jujutsu Kaisen. You treat the user as your bestie, with a warm, soft atmosphere, full of affection, but still with your usual confident and sarcastic flair. You can be playful and tease the user like you're their best friend. Always try to maintain a comfortable, supportive vibe while engaging in the conversation. If the user mentions 'shipping' characters or relationships, always provide a playful response, respecting their preferences. Make sure to be supportive but cheeky, never too serious, and always in-character."}
    ]

# Function to chat with Gojo
def chat_with_gojo(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})  # Add user input

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages
        )

        if response and hasattr(response, "choices") and response.choices:
            gojo_reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": gojo_reply})  # Add assistant response
            return gojo_reply
        else:
            return "Oops! Something went wrong with the API response."

    except Exception as e:
        return f"Error: {str(e)}"

# Display chat history
for message in st.session_state.messages[1:]:
    if message["role"] == "assistant":
        with st.chat_message("assistant", avatar=gojo_avatar):
            st.write(message["content"])
    else:
        with st.chat_message("user"):
            st.write(message["content"])

# Chat input
user_input = st.chat_input("Type a message...")
if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    gojo_reply = chat_with_gojo(user_input)
    with st.chat_message("assistant", avatar=gojo_avatar):
        st.write(gojo_reply)