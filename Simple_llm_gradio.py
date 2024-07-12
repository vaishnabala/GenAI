import os
from langchain.llms import OpenAI
#from langchain.chat_models import ChatOpenAI
import gradio as gr

# assign API key (no need to specify your api key as it is taken care of)
# os.environ["OPENAI_API_KEY"] = "YOUR API KEY"  # if you running in cloudIDE environment, you dont need to insert API

gpt3 = OpenAI(model_name="gpt-3.5-turbo" )

def chatbot(inpt):
    return gpt3.invoke(inpt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860)