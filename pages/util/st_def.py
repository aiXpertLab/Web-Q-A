import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

def st_sidebar():
    st.sidebar.image("sslogo.png", use_column_width=True)

    with st.sidebar:
        store_link = st.text_input("Enter Your Store URL:",   value="http://hypech.com/StoreSpark", disabled=True, key="store_link")
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        st.write("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        add_vertical_space(5)
        st.write('Made with ❤️ by [aiXpertLab](https://hypech.com)')

    return openai_api_key
