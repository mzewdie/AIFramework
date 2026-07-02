AIFramework v0.1.0

Overview

AIFramework is a lightweight Python framework for building AI-powered applications independently of a specific LLM provider.

Current Architecture

Application
    │
    ▼
Chatbot (planned)
    │
    ▼
AIEngine
    │
    ▼
ClientFactory
    │
    ▼
GeminiClient
    │
    ▼
Gemini API

Supporting Components

- Conversation
  Stores the complete conversation history.

- PromptBuilder
  Builds the message list sent to the AI.

- Configuration
  Loads provider, model and API key.

- ClientFactory
  Creates the correct provider implementation.

- GeminiClient
  Converts the internal message format into the Gemini SDK format.

Design Principles

- Single Responsibility Principle
- Provider Independence
- Dependency Separation
- Simple Public API