from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama   # 3rd Party Integration
import streamlit as st

# Define the prompt template with system and user messages
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Set page title and description
st.set_page_config(page_title="Ollabot - Chatbot", layout="wide")

# Set up the Streamlit web interface
st.title('Ollabot - LangChain Chatbot with Ollama LLM')
st.markdown("""
Welcome to the **LangChain Chatbot** powered by **Ollama's LLaMA** model. 
Enter a topic or question below, and the assistant will provide you with a helpful response.
""")


# Add circular LinkedIn photo using HTML and CSS
linkedin_image_url = "https://media.licdn.com/dms/image/v2/D4D03AQGgpAx6pUJCXw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1696796667460?e=1731542400&v=beta&t=9dVlSMnDqqYTdAcBM69zTx12apE66b1OxWGrcXBMH4A"

# Web App Title
st.markdown('''      
**Technology Used:** App build in `Python` + `Streamlit` using **Ollama LLM**

''')

# Display LinkedIn link followed by circular image
st.markdown(
    f'''
    <div style="display: flex; align-items: center;">
        <span>Created by <a href="https://www.linkedin.com/in/sanjeev-kumar-singh-sks-b7b612ba/" target="_blank">Sanjeev Kumar Singh</a></span>
        <img src="{linkedin_image_url}" style="border-radius: 50%; width: 30px; height: 30px; object-fit: cover; margin-left: 10px;">
    </div>
    
    ---
    ''',
    unsafe_allow_html=True
)

input_text = st.text_input("Enter your question or topic:")

# Initialize the Ollama LLM with the specified model
# Ensure that "llama3" is the correct model name available in your Ollama setup
llm = Ollama(model="llama3")

# Initialize the output parser to convert LLM output to string
output_parser = StrOutputParser()

# Create the processing chain: prompt → LLM → parser
chain = prompt | llm | output_parser

# If user has entered a query, process and display the response
if input_text:
    try:
        # Inject user input into the prompt and invoke the chain
        response = chain.invoke({'question': input_text})
        # Display the response in the Streamlit app
        st.success("**Response:**")
        st.write(response)
    except Exception as e:
        # Handle and display any errors that occur
        st.error(f"An error occurred: {e}")
