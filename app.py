import streamlit as st
import os
from dotenv import load_dotenv
from src.core.chatbot import HCPChatbot
from src.utils.config import Config

load_dotenv()

st.set_page_config(
    page_title="HCP Technical Support FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

def initialize_chatbot():
    """Initialize the chatbot with configuration."""
    if 'chatbot' not in st.session_state:
        config = Config()
        st.session_state.chatbot = HCPChatbot(config)
        st.session_state.messages = []

def main():
    st.title("🤖 HCP Technical Support FAQ Chatbot")
    st.markdown("---")
    
    initialize_chatbot()
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Check if FAQ data is loaded
        if hasattr(st.session_state.chatbot, 'vector_store') and st.session_state.chatbot.vector_store:
            st.success("✅ FAQ Database Loaded")
            st.info(f"📊 {st.session_state.chatbot.get_faq_count()} FAQ entries available")
        else:
            st.warning("⚠️ FAQ Database Not Loaded")
            if st.button("🔄 Load FAQ Database"):
                with st.spinner("Loading FAQ database..."):
                    st.session_state.chatbot.load_faq_database()
                st.rerun()
        
        st.markdown("---")
        
        # Clear conversation button
        if st.button("🗑️ Clear Conversation"):
            st.session_state.messages = []
            st.rerun()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask your HCP technical question..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Searching FAQ database..."):
                response = st.session_state.chatbot.get_response(prompt)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()