from aiframework.gemini_client import GeminiClient
from aiframework.openai_client import OpenAIClient


class ClientFactory:

    @staticmethod
    def create(config):

        if config.provider == "gemini":
            return GeminiClient(config)
        if config.provider == "openai":
            return OpenAIClient(config)

        raise ValueError(
            f"Unknown provider: {config.provider}"
        )