import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="ZapGPT")

# Replicate Credentials
with st.sidebar:
    st.title('ZapGPT')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
            st.error('Please enter a valid Replicate API token!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    os.environ['REPLICATE_API_TOKEN'] = replicate_api

    temperature = st.sidebar.slider('Temperature', min_value=0.01, max_value=2.0, value=0.7, step=0.01)
    top_p = st.sidebar.slider('Top-p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('Max Length', min_value=32, max_value=128, value=120, step=8)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLamA response. Refactored from https://github.com/a16z-infra/llama2-chatbot
def generate_llama_response(prompt_input):
    message_history = []
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            message_history.append(f"User: {dict_message['content']}")
        else:
            message_history.append(f"Assistant: {dict_message['content']}")
    
    string_dialogue = "\n\n".join(message_history)
    
    try:
        output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
                               input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                      "temperature": temperature, "top_p": top_p, "max_length": max_length, "repetition_penalty": 1})
        return output
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama_response(prompt)
            if response:
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
                message = {"role": "assistant", "content": full_response}
                st.session_state.messages.append(message)
