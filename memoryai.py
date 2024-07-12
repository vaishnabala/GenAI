# Import necessary libraries
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory, CombinedMemory, ConversationSummaryMemory
import os
import gradio as gr
import time


# Set up conversation memory
# This memory will store the last k turns of conversation
conv_memory = ConversationBufferWindowMemory(
    memory_key="chat_history_lines",
    input_key="input",
    k=1
)

# This memory will store a summary of the conversation
summary_memory = ConversationSummaryMemory(llm=OpenAI(), input_key="input")

# Combine the two memories
memory = CombinedMemory(memories=[conv_memory, summary_memory])

# Define the template for the conversation prompt
_DEFAULT_TEMPLATE = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Summary of conversation:
{history}
Current conversation:
{chat_history_lines}
Human: {input}
AI:"""

# Create the prompt from the template
PROMPT = PromptTemplate(
    input_variables=["history", "input", "chat_history_lines"], template=_DEFAULT_TEMPLATE
)

# Set up the language model
llm = OpenAI(model_name="gpt-3.5-turbo" )

# Set up the conversation chain
# This object will handle the conversation flow
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=memory,
    prompt=PROMPT
)

# Set up the Gradio interface
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()  # The chatbot object
    msg = gr.Textbox()  # The textbox for user input
    clear = gr.Button("Clear")  # The button to clear the chatbox

    # Define the function that will handle user input and generate the bot's response
    def respond(message, chat_history):
        bot_message = conversation.run(message)  # Run the user's message through the conversation chain
        chat_history.append((message, bot_message))  # Append the user's message and the bot's response to the chat history
        time.sleep(1)  # Pause for a moment
        return "", chat_history  # Return the updated chat history

    # Connect the respond function to the textbox and chatbot
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

    # Connect the "Clear" button to the chatbot
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch(server_name="0.0.0.0", server_port= 7860)