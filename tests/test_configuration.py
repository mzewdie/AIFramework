from aiframework.configuration import Configuration

config = Configuration()

print(config.provider)
print(config.model)
print(config.api_key)
#print(config.api_key[:8] + "...")