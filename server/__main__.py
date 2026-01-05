from .config import DevelopmentConfiguration

print('Running')
dev_config = DevelopmentConfiguration()
print(dev_config.AWS_USERNAME)
print(dev_config.AWS_PASSWORD)
print(dev_config.HOST)
print(dev_config.PORT)