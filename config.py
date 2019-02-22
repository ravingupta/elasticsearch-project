import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  DEVELOPMENT = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'thisisasecretcode'
  # Logging
  LOG_FILE = "logs/debug.log"
  LOG_LEVEL = "DEBUG"
  LOGGING = False

class ProductionConfig(Config):
  # MongoDB Connection
  MONGODB_HOST = '127.0.0.1'
  MONGODB_PORT = 27017
  MONGODB_DB = 'searchbar'
  MONGODB_USERNAME = 'searchbaruser'
  MONGODB_PASSWORD = 'searchbaruser'

class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = False
  LOGGING = True
  # MongoDB Connection
  MONGODB_HOST = '127.0.0.1'
  MONGODB_PORT = 27017
  MONGODB_DB = 'searchbar'
  MONGODB_USERNAME = 'searchbaruser'
  MONGODB_PASSWORD = 'searchbaruser'

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True
  LOGGING = True
  # MongoDB Connection
  MONGODB_HOST = '127.0.0.1'
  MONGODB_PORT = 27017
  MONGODB_DB = 'searchbar'
  MONGODB_USERNAME = 'searchbaruser'
  MONGODB_PASSWORD = 'searchbaruser'