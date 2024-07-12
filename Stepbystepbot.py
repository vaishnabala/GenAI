from langchain import PromptTemplate
from langchain.llms import OpenAI
import gradio as gr

# initialize the models
llm = OpenAI(
    model_name="gpt-3.5-turbo"
)

def chatbot(user_input):
    # defining a template
    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return llm.invoke(formated_prompt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch()  