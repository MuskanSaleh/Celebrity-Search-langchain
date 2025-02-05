import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

import streamlit as st

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#streamlit framework
st.title('LangChain Demo with openai api')
input_text = st.text_input("Search the topic u want")

#Open AI llms
llm = OpenAI(temperature=0.8)#

if input_text:
    st.write(llm(input_text))
    
    