from aiframework.chatbot import Chatbot

chatbot = Chatbot()

print("Welcome to AIFramework!")
print("Type 'exit' to quit.\n")

#chatbot.set_system_prompt("You are a helpful assistant.")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    messages = [
        {
        "role": "user",
        "content": question
        }
    ]

    print(f"messages pass over: {messages}")

    answer = chatbot.ask(question)
    
    

    print(f"AI: {answer}\n")