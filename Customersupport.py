
import gradio as gr
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# setting up the LLM

os.environ["OPENAI_API_KEY"] = "YOUR API KEY"
llm = OpenAI(
    model_name="gpt-3.5-turbo"
)

def handle_complaint(complaint: str) -> str:
    #Create an instance of the LLM with a temperature value of 0.9 (higher values make the output more random).
     llm.invoke(complaint,temperature=0.9)

    # Define the prompt template for the complaint handling
    prompt = PromptTemplate(input_variables=["complaint"], template="I am a customer service representative. I received the following complaint: {complaint}. My response is:")

    # Create a language model chain with the defined prompt template
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(complaint)

# Create a Gradio interface for the handle_complaint function
iface = gr.Interface(fn=handle_complaint, inputs="text", outputs="text")
iface.launch()