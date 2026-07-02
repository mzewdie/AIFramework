from aiframework.conversation import Conversation
from aiframework.prompt_builder import PromptBuilder
from aiframework.configuration import Configuration
from aiframework.client_factory import ClientFactory
from aiframework.ai_engine import AIEngine

class Chatbot:

    def __init__(self):

        self._conversation = Conversation()

        self._prompt_builder = PromptBuilder()
        
       
        config = Configuration()

        client = ClientFactory.create(config)

        self._engine = AIEngine(client)
     
        
    def set_system_prompt(self, prompt):
        self._prompt_builder.set_system_prompt(prompt)   
    
    def ask(self, question):
        self._conversation.add_user_message(question)
        messages = self._prompt_builder.build_messages(self._conversation.get_messages())
        answer = self._engine.ask(messages)
        self._conversation.add_assistant_message(answer)
        return answer