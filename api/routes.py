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
   
   - /data
       - GET: return all items
       - POST: create a new item
   
   - /data/:id
       - GET    : get item
       - PUT    : update item
       - DELETE : delete item
"""

"""
Flask-RestX models Request & Response DATA
"""

# Used to validate input data for creation
create_model = rest_api.model('CreateModel', {"code": fields.String(required=True, min_length=2, max_length=64),
                                              "name": fields.String(required=True, min_length=2, max_length=128),
                                              "value": fields.Integer(required=True),
                                              "currency": fields.String(required=True, min_length=3, max_length=3),
                                              "type": fields.String(required=False, default='transaction'),
                                            })

# Used to validate input data for update
update_model = rest_api.model('UpdateModel', {"code": fields.String(required=False, min_length=2, max_length=64),
                                              "name": fields.String(required=False, min_length=2, max_length=128),
                                              "value": fields.Integer(required=False),
                                              "currency": fields.String(required=False, min_length=3, max_length=3),
                                              "type": fields.String(required=False, default='transaction'),
                                            })

# Used to validate input data for single field supdate
update_field_model = rest_api.model('UpdateFieldModel', {"data_name" : fields.String(required=True, min_length=1, max_length=128),
                                                         "data_value": fields.String(required=True, min_length=1, max_length=128)
                                            })

"""
    Return Files - Served by @APP object
"""

@app.route('/api/from_file')
def api_from_file(): 
    return send_from_directory(os.path.join(app.root_path, 'static', 'datatables'), 'data.json')

"""
    Flask-Restx routes
"""

"""
class Data(db.Model):


    id = db.Column(db.Integer, primary_key=True)

    code     = db.Column(db.String(64))   # product code 
    name     = db.Column(db.String(128))  # product name
    value    = db.Column(db.Integer)      # numeric
    currency = db.Column(db.String(10))   # string: usd, euro
    type     = db.Column(db.String(64))   # transaction

    ts       = db.Column(db.Integer, default=datetime.utcnow().timestamp())

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

    """
       Create new item
    """
    @rest_api.expect(create_model, validate=True)
    def post(self):

        # Read ALL input  
        req_data = request.get_json()

        code     = req_data.get("code")
        name     = req_data.get("name")
        value    = req_data.get("value")
        currency = req_data.get("currency")
        type     = req_data.get("type")

        # Create new object
        new_item = Data(code=code, name=name, value=value, currency=currency, type=type)

        # Save the data
        new_item.save()
        
        response = app.response_class(
            response=json.dumps( new_item.toDICT() ),
            status=200,
            mimetype='application/json'
        )

        return response

@rest_api.route('/api/data/<int:id>')
class ItemManager(Resource):

    """
       Return Item
    """
    def get(self, id):

        response_data = []
        status = 400

        item = Data.get_by_id(id)

        if item:
            status = 200
            response_data = item.toDICT()

        response = app.response_class(
            response=json.dumps( response_data ), 
            status=status,
            mimetype='application/json'
        )

        return response

    """
       Update Item
    """
    @rest_api.expect(update_model, validate=True)
    def put(self, id):

        response_data = []
        status = 400

        # Read ALL input  
        req_data = request.get_json()

        item = Data.get_by_id(id)

        if item:
            
            status = 200
            
            # Update data
            if req_data.get("code"):
                item.code = req_data.get("code")
            
            if req_data.get("name"):
                item.name = req_data.get("name")
            
            if req_data.get("value"):
                item.value = req_data.get("value")
            
            if req_data.get("currency"):
                item.currency = req_data.get("currency")
            
            if req_data.get("type"):
                item.type = req_data.get("type")

            # Save the data
            item.save()

            response_data = item.toDICT()

        response = app.response_class(
            response=json.dumps( response_data ), 
            status=status,
            mimetype='application/json'
        )

        return response

    """
       Delete Item
    """
    def delete(self, id):

        response_data = []
        status = 400

        item = Data.get_by_id(id)

        if item:
            
            status = 200

            # Delete and save the change
            Data.query.filter_by(id=id).delete()
            db.session.commit()

        response = app.response_class(
            response=json.dumps( response_data ), 
            status=status,
            mimetype='application/json'
        )

        return response

@rest_api.route('/api/data/field/<int:id>')
class FieldManager(Resource):

    """
       Return Item
    """
    @rest_api.expect(update_field_model, validate=True)
    def put(self, id):

        response_data = []
        status = 400

        # Read ALL input  
        req_data = request.get_json()

        item = Data.get_by_id(id)

        if item:
            
            status = 200
            
            data_name  = req_data.get("data_name"  )
            data_value = req_data.get("data_value" )
            
            if data_name == 'code':
                item.code = data_value        

            if data_name == 'name':
                item.name = data_value        

            # Save the data
            item.save()

            response_data = item.toDICT()

        response = app.response_class(
            response=json.dumps( response_data ), 
            status=status,
            mimetype='application/json'
        )

        return response     