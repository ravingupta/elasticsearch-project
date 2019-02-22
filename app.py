import os
from flask import Flask, Response, request, jsonify, abort
from flask_mongoengine import MongoEngine
from flask_cors import CORS

from controllers import *

# Flask Setup
app = Flask(__name__)
CORS(app)

# Registering all the routes from controllers using blueprint
app.register_blueprint(search_api)

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

# Import models to access database if required
# from models import *

# Sample Route URL
@app.route("/")
def hello():
  return jsonify({"success": 1, "message": "Hello World!", "data": {"server_type": PYTHON_SERVER}}), 200

# Handle Every Server Failure
@app.errorhandler(500)
def server_error(e):
  return ("""
  An internal error occurred: <pre>{}</pre>
  """.format(e), 500,)

# Handle Every Authorization Failure
@app.errorhandler(404)
def notfound_error(e=""):
  return ("""
  <h3>404 Page Not Found</h3>
  """, 404,)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)