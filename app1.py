from flask import Flask, jsonify, request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager, UserMixin, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

import os

app = FlaskAPI(__name__)
login = LoginManager(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/stem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  description = db.Column(db.String(250))
  password_hash = db.Column(db.String(128))

  def __init__(self, id_, name, email, description):
    self.id = id_
    self.name = name
    self.email = email
    self.description = description

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(250))
  category = db.Column(db.String(50))
  topic = db.Column(db.String(50))
  body = db.Column(db.String(5000))
  tags = db.Column(db.String(200))
  upvote = db.Column(db.Integer)
  Registered = Column(DateTime, nullable = False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __init__(self, name, description, category, topic, body, tags):
    self.name = name
    self.description = description
    self.category = category
    self.topic = topic
    self.body = body
    self.tags = tags

class Category(db.Model):
  __tablename__ = 'category'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)

  def __init__(self, name):
    self.name = name

class Comment(db.Model):
  __tablename__ = 'category'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150))
  body = db.Column(db.String
  Registered = Column(DateTime, nullable = False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
  upvote = db.Column(db.Integer)
  downvote = db.Column(db.Integer)

  def __init__(self, title, body, upvote, downvote):
    self.title = title
    self.body = body
    self.upvote = upvote
    self.downvote = downvote

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'description')

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'category', 'topic', 'body', 'tags')

class CommentSchema(ma.Schema):
  class Meta:
    fields = ('id', 'title', 'body')

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

