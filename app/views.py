# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 
from datetime import datetime

# Flask modules
from flask   import render_template, request, send_from_directory
from jinja2  import TemplateNotFound
from api.models import Data

# App modules
from app import app

'''
DATA tables routes
'''

# DataTables processed in controler
@app.route('/datatables/')
def datatables():

    # Expected Data
    '''
    <table class="table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Ext.</th>
                <th>City</th>
                <th data-type="date" data-format="YYYY/DD/MM">Start Date</th>
                <th>Completion</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Unity Pugh</td><td>9958</td><td>Curicó</td><td>2005/02/11</td><td>37%</td></tr>
            <tr><td>Theodore Duran</td><td>8971</td><td>Dhanbad</td><td>1999/04/07</td><td>97%</td></tr>
            <tr><td>Kylie Bishop</td><td>3147</td><td>Norman</td><td>2005/09/08</td><td>63%</td></tr>
            <tr><td>Willow Gilliam</td><td>3497</td><td>Amqui</td><td>2009/29/11</td><td>30%</td></tr>
            <tr><td>Blossom Dickerson</td><td>5018</td><td>Kempten</td><td>2006/11/09</td><td>17%</td></tr>
        </tbody>
    </table>
    '''
    
    '''
    Data:
        id = db.Column(db.Integer, primary_key=True)

        code     = db.Column(db.String(64))   # product code 
        name     = db.Column(db.String(128))  # product name
        value    = db.Column(db.Integer)      # numeric
        currency = db.Column(db.String(10))   # string: usd, euro
        type     = db.Column(db.String(64))   # transaction
        ts       = db.Column(db.Integer, default=datetime.utcnow().timestamp())    
    '''

    table  = ''
    table += '<table class="table hoverTable">'
    table += '    <thead>'
    table += '        <tr>'
    table += '            <th>ID</th>'
    table += '            <th>Product Code</th>'
    table += '            <th>Description</th>'
    table += '            <th>Price</th>'
    table += '            <th>Currency</th>'
    table += '            <th>Timestamp</th>'
    table += '            <th>&nbsp;</th>'
    table += '        </tr>'
    table += '    </thead>'
    table += '    <tbody>'
    
    # Sample
    # table += '        <tr><td>1</td><td>PRD_CODE</td><td>PRD_INFO</td><td>99</td><td>usd</td><td>2022-02-03</td></tr>'
    
    for item in Data.query.all():    

        # Format the date
        ts = datetime.utcfromtimestamp(item.ts).strftime('%Y-%m-%d')
       #table += '        <tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>'.format( item.id, item.code, item.name, item.value, item.currency, ts )
        
        # Open ROW
        table += '<tr data-id="' + str( item.id   ) + '" class="editable">'
        
        table += '<td data-name="id">' + str( item.id   )  + '</td>' # ID
        table += '<td class="editable" data-name="code">' + item.code         + '</td>' # ID
        table += '<td class="editable" data-name="name">' + item.name         + '</td>' # ID
        table += '<td class="editable" data-name="value">' + str( item.value ) + '</td>' # ID
        table += '<td class="editable" data-name="currency">' + item.currency     + '</td>' # ID
        table += '<td data-name="ts">' + ts                + '</td>' # ID

        table += '<td><a href="#" class="row-delete text-danger me-3">delete</a></td>' # ID

        # Close ROW
        table += '</tr>'

    table += '    </tbody>'
    table += '</table>' 
    
    return render_template( 'datatables/datatables.html', segment='datatables', table=table )

# DataTables lazy loaded via API
@app.route('/datatables-api/')
def datatables_api():

    return render_template( 'datatables/datatables-via-api.html', segment='datatables-api' )

# DataTables lazy loaded via API
@app.route('/datatables-from-file/')
def datatables_from_file():

    return render_template( 'datatables/datatables-via-file.html', segment='datatables-from-file' )

# App main route + generic routing
@app.route('/')
def index():

    return render_template( 'index.html', segment='index.html' )

# App main route + generic routing
@app.route('/<path>')
def pages(path):

    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( 'pages/' + path, segment=segment )
    
    except TemplateNotFound:
        return render_template('pages/page-404.html'), 404

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
