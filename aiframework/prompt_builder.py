class PromptBuilder:

    def __init__(self, system_prompt):
        self._system_prompt = system_prompt

    def build_messages(self, messages, question):
        
        prompt_messages = [
            {
                "role": "system",
                "content": self._system_prompt
            }
        ]

        prompt_messages.extend(messages)

        prompt_messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        return prompt_messages