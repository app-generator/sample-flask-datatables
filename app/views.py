# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 

# Flask modules
from flask   import render_template, request, send_from_directory
from jinja2  import TemplateNotFound

# App modules
from app import app

# Return sitemap
@app.route('/api')
def sitemap(): 
    return send_from_directory(os.path.join(app.root_path, 'static', 'datatables'), 'demo.json')

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):

    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( path, segment=segment )
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
