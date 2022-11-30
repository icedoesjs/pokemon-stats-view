# Open and load YAML config file
import yaml
import secrets
key = secrets.token_urlsafe(16)
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    

# Create config class 
class Config():
    def __init__(self):
        self.config = config
        self.secret_key = key