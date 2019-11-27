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

# Test
@app.route('/', methods=['GET'])
def get():
    return ({ 'msg': 'stempedia.org in the house'})


# Run Server
if __name__ == '__main__':
    manager.run()