# import streamlit as st
# import groq
# import os
# st.set_page_config(page_title="Gojo Chatbot 💙", layout="wide")
# st.title("💙 Talk to Gojo Satoru!")
# # Set up the Groq client

# client = groq.Client(api_key="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")

# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#         body {
#             background-color: #0d0d0d; /* Dark theme */
#             color: white;
#         }
#         .stChatMessage {
#             padding: 10px;
#             border-radius: 10px;
#             margin: 5px 0;
#         }
#         .user-msg {
#             background-color: #007bff;
#             color: white;
#             text-align: right;
#         }
#         .gojo-msg {
#             background-color: #5a189a;
#             color: white;
#         }
#         .chat-container {
#             max-width: 700px;
#             margin: auto;
#         }
#         .gojo-avatar {
#             content: url('https://i.imgur.com/Q1q9qAs.png'); /* Gojo PFP */
#             width: 40px;
#             height: 40px;
#             border-radius: 50%;
#             margin-right: 10px;
#         }
#         .user-avatar {
#             content: url('https://i.imgur.com/7R5dsFS.png'); /* Default User PFP */
#             width: 40px;
#             height: 40px;
#             border-radius: 50%;
#             margin-left: 10px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "system", "content": "You are Gojo Satoru from Jujutsu Kaisen. You treat the user as your bestie, with a warm, soft atmosphere, full of affection, but still with your usual confident and sarcastic flair. You can be playful and tease the user like you're their best friend. Always try to maintain a comfortable, supportive vibe while engaging in the conversation. If the user mentions 'shipping' characters or relationships, always provide a playful response, respecting their preferences. Make sure to be supportive but cheeky, never too serious, and always in-character."}
#     ]

# # Function to chat with Gojo
# def chat_with_gojo(prompt):
#     st.session_state.messages.append({"role": "user", "content": prompt})  # Add user input

#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=st.session_state.messages
#     )

#     if hasattr(response, "choices") and response.choices:
#         gojo_reply = response.choices[0].message.content
#         st.session_state.messages.append({"role": "assistant", "content": gojo_reply})  # Add assistant response
#         return gojo_reply
#     else:
#         return "Oops! Something went wrong with the API response."

# # Display chat history
# for message in st.session_state.messages[1:]:  # Skip system message
#     avatar = "gojo-avatar" if message["role"] == "assistant" else "user-avatar"
#     css_class = "gojo-msg" if message["role"] == "assistant" else "user-msg"
    
#     with st.chat_message(message["role"]):
#         st.markdown(f"""
#             <div class="chat-container">
#                 <span class="{avatar}"></span>
#                 <div class="{css_class}">{message["content"]}</div>
#             </div>
#         """, unsafe_allow_html=True)

# # Chat input field
# user_input = st.chat_input("Type a message...")
# if user_input:
#     with st.chat_message("user"):
#         st.write(user_input)

#     gojo_reply = chat_with_gojo(user_input)

#     with st.chat_message("assistant"):
#         st.write(gojo_reply)
import streamlit as st
import groq
import os

st.set_page_config(page_title="Gojo Chatbot 💙", layout="wide")
st.title("💙 Talk to Gojo Satoru!")

# Secure API Key

client = groq.Client(api_key="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")

def load_css(css_file):
    with open(css_file, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load Custom CSS
load_css("styles.css")

# ---- Title ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            fotter {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

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
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            st.image("image.png", width=40)  # Gojo PFP
        else:
            st.image("image2.png", width=40)  # User PFP

        st.write(message["content"])

# Chat input field
user_input = st.chat_input("Type a message...")
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    gojo_reply = chat_with_gojo(user_input)

    with st.chat_message("assistant"):
        st.write(gojo_reply)
