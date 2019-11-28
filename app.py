from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from datetime import datetime
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/stem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
# Configure app settings with migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

## CLASSES
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
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
    user = db.column(db.Integer())

    def __init__(self, name, description, category, topic, body, tags, date, user): 
        self.name = name
        self.description = description
        self.category = category
        self.topic = topic
        self.body = body
        self.tags = tags
        self.date = date
        self.user = user


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name


## SCHEMA
class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'category', 'topic', 'body', 'tags', 'date', 'user')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'description')

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

#INIT SCHEMA
user_schema = UserSchema()
users_schema = PostSchema(many=True)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

## ROUTES
## Create User
@app.route('/user', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    description = request.json['description']

    new_user = User(name, email, description)

    ## add to db
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

## Create Post
@app.route('/post', methods=['POST'])
def add_post():
    name = request.json['name']
    description = request.json['description']
    category = request.json['category']
    topic = request.json['topic']
    body = request.json['body']
    tags = request.json['tags']
    date = request.json['date']
    user = request.json['user']

    new_post = Post(name, description, category, topic, body, tags, date, user)

    ## add to db
    db.session.add(new_post)
    db.session.commit()

    return post_schema.jsonify(new_post)



# Run Server
if __name__ == '__main__':
    manager.run()

# # Test
# @app.route('/', methods=['GET'])
# def get():
#     return ({ 'msg': 'stempedia.org in the house'})