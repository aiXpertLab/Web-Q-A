import streamlit as st, openai 
from typing import List, Optional
from pages.util import st_def, openaipdf

st.set_page_config(page_title='🦜🔗 Text Summarization App')
st.title('🦜🔗 Text Summarization App')
openai_api_key= st_def.st_sidebar()

client = openaipdf.PDFChat()

loader = PyPDFLoader("example_data/layout-parser-paper.pdf")
pages = loader.load_and_split()

def generate_response(txt):
    llm = OpenAI(model="gpt-3.5-turbo-0125", temperature=0, openai_api_key=openai_api_key)      # Instantiate the LLM model
    text_splitter = CharacterTextSplitter()                     # Split text
    texts = text_splitter.split_text(txt)
    docs = [Document(page_content=t) for t in texts]            # Create multiple documents
    chain = load_summarize_chain(llm, chain_type='map_reduce')      # Text summarization

    return chain.run(docs)

# Text input
txt_input = st.text_area('Copy/paste or enter your text', '', height=200)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')

    if not openai_api_key:
        st.info("⬅️Please add your OpenAI API key to continue.")
    elif submitted:
        try:
            with st.spinner('Calculating...'):
                response = generate_response(txt_input)
                result.append(response)
        except:
            st.info("Invalid OpenAI API key. Please enter a valid key to proceed.")

if len(result):
    st.info(response)