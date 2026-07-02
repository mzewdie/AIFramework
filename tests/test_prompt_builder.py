import unittest
from aiframework.conversation import Conversation
from aiframework.prompt_builder import PromptBuilder


conversation = Conversation()

conversation.add_user_message("Hello")
conversation.add_assistant_message("Hi Mulugeta!")

builder = PromptBuilder("You are a Python tutor.")

messages = builder.build_messages(
    conversation.get_messages(),
    "Explain loops."
)

for message in messages:
    #print(f"Number of Messages: {len(messages)}")
    print(message)
    
assert len(messages)==4    