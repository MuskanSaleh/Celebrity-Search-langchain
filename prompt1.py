import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

# Ensure API key is set correctly
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("Celebrity Search Results")
input_text = st.text_input("Enter a celebrity's name:")

# Prompt template
first_prompt = PromptTemplate(
    input_variables=["celebrity_name"],
    template="Tell me about the celebrity {celebrity_name} in a few sentences."
)

# Use ChatOpenAI instead of OpenAI (because gpt-3.5-turbo is a chat model)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.8)

# Create the LLM chain
chain = LLMChain(llm=llm, prompt=first_prompt, verbose=True)

# Run the chain if the user provides input
if input_text:
    response = chain.run({"celebrity_name": input_text})
    st.write(response)
