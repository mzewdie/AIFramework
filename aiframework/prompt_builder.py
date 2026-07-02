class PromptBuilder:

    def __init__(self):
        self._system_prompt = None
        

    #def build_messages(self, messages, question):
    def build_messages(self, conversation_messages):
         prompt_messages = []
       
         if self._system_prompt:
             prompt_messages.append (
                 {
                   "role": "system",
                   "content": self._system_prompt
                }
             )     
         prompt_messages.extend(conversation_messages)
         return prompt_messages
    
    def set_system_prompt(self, prompt):
        self._system_prompt = prompt