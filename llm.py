import streamlit as st
from langchain_community.llms import OpenAI
import tiktoken

# Set page title and favicon
st.set_page_config(page_title="PharmaBot", page_icon=":pill:")

# Page title
st.title('PharmaBot - Your Pharmaceutical Support Chatbot')

# Sidebar for API key input
openai_api_key = st.sidebar.text_input('Enter your OpenAI API key')

# Function to count tokens
def count_tokens(string: str) -> int:
    # Load the encoding for gpt-3.5-turbo (which uses cl100k_base)
    encoding_name = "p50k_base"
    encoding = tiktoken.get_encoding(encoding_name) 
    # Encode the input string and count the tokens
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Function to generate response
def generate_response(input_text):
    try:
        # Check if API key is provided
        if openai_api_key.startswith('sk-'):
            llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
            response = llm(input_text)
            num_tokens = count_tokens(input_text)
            st.info(f"Input contains {num_tokens} tokens.")
            st.info(response)
        else:
            st.warning('Please enter your OpenAI API key!', icon='🔒')
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Form for text input and submit button
with st.form('my_form'):
    text = st.text_area('Enter your query:', 'How can I use this medication safely?')
    submitted = st.form_submit_button('Submit')

# Generate response upon form submission
if submitted:
    generate_response(text)

# Footer with company information
st.markdown("""
---
PharmaBot is provided by Teva Pharmaceuticals.
For more information, visit [Teva Pharmaceuticals website](https://www.tevapharm.com/).
""")
