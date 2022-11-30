from flask import Flask
site = Flask(__name__)
from config import Config
from .auth.routes import auth

# Add all items to site config 
config_instance = Config()
config = config_instance.__dict__
site.config["SECRET_KEY"] = config["secret_key"]
for key, value in config["config"].items():
    site.config[key.upper()] = value
    
# Register Blueprint
site.register_blueprint(auth)

from . import routes