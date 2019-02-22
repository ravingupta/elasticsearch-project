""" Database models for Posts """

from flask_mongoengine import MongoEngine

db = MongoEngine()

class Posts(db.Document):
  title = db.StringField(required=True, unique=True)
  body = db.StringField()

  user_id = db.IntField()