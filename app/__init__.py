# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


# import Flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api import rest_api

# Inject Flask magic
app = Flask(__name__)

# Load the configuration
app.config.from_object('app.config.Config')

# Bind Flask-SqlAlchemy
db = SQLAlchemy(app) 

# Create Tables
@app.before_first_request
def initialize_database():
    db.create_all()

# Import routing to render the pages
from app import views

# Bind Flask-RestX
rest_api.init_app(app)

# Import API Routes
from api import routes
