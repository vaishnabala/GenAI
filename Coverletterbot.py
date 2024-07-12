
import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain.llms import OpenAI

# you dont need to insert API
openai_api_key = ""
os.environ["OPENAI_API_KEY"] = openai_api_key

# initialize the models
llm = OpenAI(
    model_name="gpt-3.5-turbo"
)

# Define a PromptTemplate to format the prompt with user input
prompt = PromptTemplate(
    input_variables=["position", "company", "skills"],
    template="Dear Hiring Manager,\n\nI am writing to apply for the {position} position at {company}. I have experience in {skills}.\n\nThank you for considering my application.\n\nSincerely,\n[Your Name]",
)

# Define a function to generate a cover letter using the llm and user input
def generate_cover_letter(position: str, company: str, skills: str) -> str:
    formatted_prompt = prompt.format(position=position, company=company, skills=skills)
    response = llm(formatted_prompt)
    return response

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Position"),
    gr.Textbox(label="Company"),
    gr.Textbox(label="Skills")
]

# Define the Gradio interface output
output = gr.Textbox(label="Cover Letter")

# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(server_name="0.0.0.0", server_port= 7860)