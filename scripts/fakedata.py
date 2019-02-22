import os, sys
sys.path.insert(0,'..')

from flask import Flask
from flask_mongoengine import MongoEngine
import requests

# Flask Setup
app = Flask(__name__)

# Check Python Server
PYTHON_SERVER = os.environ.get('PYTHON_SERVER', 'PRODUCTION')

# Configure flask
if PYTHON_SERVER == "PRODUCTION":
  app.config.from_object('config.ProductionConfig')
elif PYTHON_SERVER == "STAGING":
  app.config.from_object('config.StagingConfig')
else:
  app.config.from_object('config.DevelopmentConfig')

# Setup Mongoengine
db = MongoEngine(app)

from models import *

def init():
  r = requests.get('https://jsonplaceholder.typicode.com/posts')
  json_data = r.json()
  Posts.drop_collection()
  for data in json_data:
    Posts(title=data['title'], body=data['body'], user_id=data['userId']).save()

if __name__ == "__main__":
  init()