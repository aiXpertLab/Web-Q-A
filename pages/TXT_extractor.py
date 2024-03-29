import streamlit as st
from txtai.embeddings import Embeddings

st.set_page_config(page_title="Text Extractor", page_icon="📄")
with st.sidebar:
    st.markdown('''
    ### 📄 TXT Insights: No need to comb through pages. Extract crucial knowledge in seconds.
- upload a .txt file 
- ask questions about your txt file
- get answers from your txt file
- enjoy and support the project with a star on [Github](https://www.github.com/aiXpertLab)
    ''')

def main():
    st.header("Chat with your TXT documents")
    txt = st.file_uploader("Upload your Txt", type='txt')
    
    if txt is not None:
        _file_content = txt.getvalue().decode("utf-8")
        file_content = _file_content.splitlines()

        embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
        embeddings.index(((x, text, None) for x, text in enumerate(file_content)))

        print("%-20s %s" % ("Query", "Best Match"))
        print("-" * 150)

        query = st.text_input("Ask questions about your TXT file:")
        print(query)

        if query:
            uid = embeddings.search(query, 1)[0][0]
            print(uid)

            st.write("%-20s %s" % (query, file_content[uid]))
 
if __name__ == '__main__':
    main()