class AIEngine:

    def __init__(self, client):
        self._client = client

    def ask(self, messages):
        return self._client.ask(messages)