"""
 The class manages the conversation history.
 
 Messages are stored as python dictionaries:
 
 [
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hello Mulugeta!"
    }
]
 
"""

class Conversation:
   

    def __init__(self):
        self._messages = []

    def add_user_message(self, message):
        self._add_message("user", message)
        
    def add_assistant_message(self, message):
        self._add_message("assistant", message)

    def _add_message(self, role, content):
        self._messages.append(
        {
            "role": role,
            "content": content
        }
    )

    def get_messages(self):
        return self._messages.copy()

    def clear(self):
        self._messages.clear()