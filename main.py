import streamlit as st
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader



# Streamlit Title
st.title('Chatbot for Llama Papers')
user_input = st.text_input("Please enter your question here")


from dotenv import load_dotenv
import os
load_dotenv()


openai_api_key = os.getenv('OPENAI_API_KEY')
# Get the value of the 'OPENAI_API_KEY' environment variable.
# I have a .gitignore file





loader = TextLoader('papers.txt')

papers = loader.load()

embedding = OpenAIEmbeddings()  


