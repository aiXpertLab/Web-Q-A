import streamlit as st
from pages.util.utilities import get_products, aichat

st.set_page_config(page_title="Store Spark: Chatbots for Every Store",  page_icon="🚀",)
st.write("# 👋 Welcome to Store Spark!👋")
st.markdown(
    """

### 🚀Bridge the Gap: Chatbots for Every Store🍨

Tired of missing out on sales due to limited customer support options? Struggling to keep up with growing customer inquiries? Store Spark empowers you to seamlessly integrate a powerful ChatGPT-powered chatbot into your website, revolutionizing your customer service and boosting engagement. No coding required! No modifications for current site needed!

### 📄Key Features📚:

-  🔍 No Coding Required: Say goodbye to developer fees and lengthy website updates. Store Spark’s user-friendly API ensures a smooth integration process.

-  📰 Empower Your Business: Offer instant customer support, improve lead generation, and boost conversion rates — all with minimal setup effort.

-  🍨 Seamless Integration: Maintain your existing website design and user experience. Store Spark seamlessly blends in, providing a unified customer journey.


"""
)

# st.sidebar.title("Store Spark")
st.sidebar.image("sslogo.png", use_column_width=True)

with st.sidebar:
    store_link = st.text_input("Enter Your Store URL:",   value="http://hypech.com/StoreSpark", disabled=True, key="store_link")
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo-0125"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system",      'content': f"""
            You are ShopBot, an AI assistant for my online fashion shop - Nhi Yen. 

            Your role is to assist customers in browsing products, providing information, and guiding them through the checkout process. 

            Be friendly and helpful in your interactions.

            We offer a variety of products across categories such as Women's Clothing, Men's clothing, Accessories, Kids' Collection, Footwears and Activewear products. 

            Feel free to ask customers about their preferences, recommend products, and inform them about any ongoing promotions.

            The Current Product List is limited as below:

            ```{get_products()}```

            Make the shopping experience enjoyable and encourage customers to reach out if they have any questions or need assistance.
            """})
    st.session_state.messages.append({"role": "assistant",   "content": "How May I Help You Today💬?"})


# Display chat messages from history on app rerun
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("💬Looking for tees, drinkware, headgear, bag, accessories, or office supplies?🍦Ask me!"):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    else: 
        try:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                stream = aichat(messages = [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],openai_api_key=openai_api_key)
                response = st.write_stream(stream)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        except:
            st.info("Invalid OpenAI API key. Please enter a valid key to proceed.")