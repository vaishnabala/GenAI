# using Hugging FaceHub
from langchain import HuggingFaceHub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "YOUR API KEY"
llm = HuggingFaceHub(repo_id="google/flan-t5-xl")
text = "tell me insteresting fact about potato"
result = llm(text)
print(result)