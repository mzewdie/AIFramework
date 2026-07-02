from aiframework.conversation import Conversation

conversation = Conversation()

conversation.add_user_message("Hello")

conversation.add_assistant_message("Hi Mulugeta!")

conversation.add_user_message("Next Message")

print("The package aiframework.conversation called")

print(conversation.get_messages())