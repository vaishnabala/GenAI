import os
from langchain.llms import OpenAI

# Set the environment variable "OPENAI_API_KEY" to your OpenAI API key. This is required to authenticate with the OpenAI API.
os.environ["OPENAI_API_KEY"] = "YOUR API KEY"

# Specifying the LLM model 
gpt3 = OpenAI(model_name="gpt-3.5-turbo" )

text = "tell me insteresting fact about potato"
print(gpt3.invoke(text))