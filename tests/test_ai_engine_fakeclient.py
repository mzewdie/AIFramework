from aiframework.ai_engine import AIEngine


class FakeClient:

    def generate(self, messages):
        return f"This is a fake response. for {messages}"


engine = AIEngine(FakeClient())

messages = [
    {
        "role": "user",
        "content": "Hello"
    }
]

response = engine.generate(messages)

print(response)