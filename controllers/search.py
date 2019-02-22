from flask import Blueprint, Response, request, abort, jsonify, g, render_template
from elasticsearch import Elasticsearch

es = Elasticsearch()

search_api = Blueprint('search_api', __name__)

from models import *

@search_api.route("/search_posts", methods=['GET', 'POST'])
def search_posts():
  q = ""
  match_data = {}
  if request.method == 'POST':
    q = request.form['q']
    query = {
      "query": {
        "match": {
          "title": q
        },
        "match": {
          "body": q
        }
      }
    }
    match_data = es.search(index="posts", doc_type="post", body=query)
  return render_template('posts/index.html', q=q, match_data=match_data)

@search_api.route("/refresh_posts", methods=['GET', 'POST'])
def refresh_posts():
  es.indices.delete(index='posts', ignore=[400, 404])
  mappings = {
    "mappings": {
      "post": {
        "properties": {
          'id': {'type': 'keyword'},
          'title': {'type': 'text'},
          'body': {'type': 'text'},
          'user_id': {'type': 'integer'}
        }
      }
    }
  }
  es.indices.create(index="posts", body=mappings)
  for post in Posts.objects.all():
    doc_body = {
      'id': str(post.id),
      'user_id': int(post.user_id),
      'title': post.title,
      'body': post.body
    }
    print(es.index(index="posts", doc_type="post", body=doc_body))
  return jsonify({"success": 1, "message": "All Indexes Refreshed", "data": {}})