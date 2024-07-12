# using Cohere
from langchain.llms import Cohere
cohere = Cohere(model='command-xlarge')

'''Modiyf the below code'''
# using Hugging FaceHub
from langchain import Hugging FaceHub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "YOUR API KEY"
llm = HuggingFaceHub(repo_id="google/flan-t5-xl")
text = "tell me insteresting fact about potato"
result = llm(text)
print(result)