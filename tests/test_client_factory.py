import aiframework
from aiframework.configuration import Configuration
from aiframework.client_factory import ClientFactory

config = Configuration()

client = ClientFactory.create(config)

print(aiframework.__version__)

print(type(client))
print(f"Provider is: {client.get_provider()}")