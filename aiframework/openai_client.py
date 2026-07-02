class OpenAIClient:
    def __init__(self,config):
        self.config=config
        
    def get_provider(self):
        return self.config.provider 