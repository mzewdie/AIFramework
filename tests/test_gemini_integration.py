from aiframework.configuration import Configuration
from aiframework.client_factory import ClientFactory
from aiframework.ai_engine import AIEngine


config = Configuration()

client = ClientFactory.create(config)

engine = AIEngine(client)

message = [
    {
        "role": "user",
        "content": "Hi Gemini, how were you yesterday?"
    }
]

print(f"messages pass over: {message}")
answer = engine.ask(message)

print(answer)