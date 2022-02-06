# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, json
from flask import request, send_from_directory
from flask_restx import Api, Resource, fields

from app import app, db
from api.models import Data
from api import rest_api

from datetime import datetime
from sqlalchemy import desc, asc

"""
API Interface:
   
   - /api/data
       - GET: return all items

   - /api/from_file
       - GET    : get item

"""

# Return Files - Served by @APP object
@app.route('/api/from_file')
def api_from_file(): 
    return send_from_directory(os.path.join(app.root_path, 'static', 'datatables'), 'data.json')

"""
    Flask-Restx routes
"""

@rest_api.route('/api/data')
class Items(Resource):

    """
       Return all items
    """
    def get(self):

        data = []
        
        for item in Data.query.all():
            data.append( item.toDICT() ) 

        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )

        return response