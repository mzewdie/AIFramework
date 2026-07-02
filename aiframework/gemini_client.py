from google import genai
from google.genai import types


class GeminiClient:

    def __init__(self, config):

        self._model = config.model
        self._config=config

        self._client = genai.Client(
            api_key=config.api_key
        )
        
    def get_provider(self):
        return "Not yet implemented"

    def ask(self, messages):
          
        contents = []

        for message in messages:
            contents.append(
                
                types.Content(
                    
                    role=message["role"],
                    parts=[types.Part.from_text(text=message["content"])]
                )
        
                )
        
        print(f"messages before convertion for the api call: {message}")
        print(f"messages converted for the api call: {contents}")
        response = self._client.models.generate_content(
            model=self._model,
            contents=contents
        )

        return response.text