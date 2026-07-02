class BaseClient:

    def generate(self, messages):
        raise NotImplementedError
    
    
    #use it as 
    # class GeminiClient(BaseClient):
    # class OpenAIClient(BaseClient):
    #....