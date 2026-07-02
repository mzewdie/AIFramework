import os

from dotenv import load_dotenv

from aiframework.constants import (
    DEFAULT_PROVIDER,
    DEFAULT_MODEL,
    ENV_PROVIDER,
    ENV_MODEL,
    ENV_GEMINI_API_KEY,
    ENV_OPENAI_API_KEY
)


class Configuration:

    def __init__(self):

        load_dotenv()

        self.provider = os.getenv(
            ENV_PROVIDER,
            DEFAULT_PROVIDER
        )

        self.model = os.getenv(
            ENV_MODEL,
            DEFAULT_MODEL
        )

        self.api_key = self._load_api_key()

    def _load_api_key(self):

        if self.provider == "gemini":
            return os.getenv(ENV_GEMINI_API_KEY)

        if self.provider == "openai":
            return os.getenv(ENV_OPENAI_API_KEY)

        return None