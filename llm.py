import streamlit as st
import openai

# Set page configuration
st.set_page_config(page_title="PharmaBot", page_icon=":pill:")

# Page title
st.title('PharmaBot - Your Pharmaceutical Support Chatbot')

# Sidebar for API key input
openai_api_key = st.sidebar.text_input('Enter your OpenAI API key', type="password")

# Function to generate response using OpenAI
def generate_response(input_text: str):
    if not openai_api_key:
        st.warning('Please enter your OpenAI API key!', icon='🔒')
        return

    if not openai_api_key.startswith('sk-'):
        st.error('Invalid API key format.')
        return

    try:
        openai.api_key = openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": input_text}]
        )
        st.info(response['choices'][0]['message']['content'])
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Input form for user query
with st.form('user_input_form'):
    text = st.text_area('Enter your query:', 'How can I use this medication safely?')
    submitted = st.form_submit_button('Submit')

    # Process the input upon form submission
    if submitted:
        generate_response(text)

# Footer with company information
st.markdown("""
---
PharmaBot is provided by Teva Pharmaceuticals.
For more information, visit [Teva Pharmaceuticals website](https://www.tevapharm.com/).
""")
