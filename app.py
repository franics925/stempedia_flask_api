from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from datetime import datetime
import os


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

## CLASSES
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    description = db.Column(db.String(100))
    def __init__(self, name, email, description):
        self.name = name
        self.email = email
        self.description = description

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(250))
    category = db.Column(db.String(50))
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    # category = db.relationship('Category', backref=db.backref('posts', lazy=True))
    topic = db.Column(db.String(50))
    body = db.Column(db.String(5000))
    tags = db.Column(db.String(200))
    date = db.Column(db.String(15))
    def __init__(self, name, description, category, topic, body, tags): 
        self.name = name
        self.description = description
        self.category = category
        self.topic = topic
        self.body = body
        self.tags = tags

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    def __init__(self, name):
        self.name = name


## SCHEMA
class PostSchema(ma.Schema):
    class Meta:
        fields= ('id', 'name', 'description', 'category', 'topic', 'body', 'tags')

class UserSchema(ma.Schema):
    class Meta:
        fields= ('id', 'name', 'email', 'description')

class CategorySchema(ma.Schema):
    class Meta:
        fields= ('id', 'name')


# Run Server
if __name__ == '__main__':
    app.run(debug=True)

# # Test
# @app.route('/', methods=['GET'])
# def get():
#     return ({ 'msg': 'stempedia.org in the house'})