import os
#from langchain.agents import load_tools
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
#from langchain.llms import OpenAI 
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

#openai_api_key = "YOUR API KEY"

#os.environ["OPENAI_API_KEY"] = openai_api_key

gpt3 = ChatOpenAI(model_name='gpt-3.5-turbo')

try:
    tools = load_tools(["llm-math", "python_repl", "requests_all", "human"], llm=gpt3)
    agent = initialize_agent(tools, llm=gpt3, agent="zero-shot-react-description", verbose=True)
except ValueError as e:
    print(f"Error loading tools: {e}")
    # Handle the error appropriately

agent.run("create simple matplotlib showing sin function and plot it")