#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:41:13 2019

@author: harriet
"""

from flask import Flask, render_template, request, jsonify
import json
import sqlite3


mock_data=[{"task_id":37,"title":"sorbitol","desc":"Cross-group","status":"Fuscia","date_due":"3/26/2018","date_created":"10/25/2018","imp":"Mauv"},
{"task_id":46,"title":"Buspirone hydrochloride","desc":"Face to face","status":"Goldenrod","date_due":"8/10/2018","date_created":"7/22/2018","imp":"Orange"},
{"task_id":64,"title":"Topiramate","desc":"bottom-line","status":"Aquamarine","date_due":"10/27/2018","date_created":"5/30/2018","imp":"Green"},
{"task_id":73,"title":"Titanium Dioxide","desc":"client-server","status":"Red","date_due":"5/23/2018","date_created":"8/27/2018","imp":"Fuscia"},
{"task_id":99,"title":"TITANIUM DIOXIDE, OCTINOXATE","desc":"Quality-focused","status":"Green","date_due":"11/12/2018","date_created":"9/28/2018","imp":"Purple"},
{"task_id":14,"title":"Ceanothus americanus, Hydrastis canadensis, Veratrum album, Anacardium orientale, Argentum nitricum, Condurango, Momordica balsamina, Oxalis acetosella, Pulsatilla, Bile duct, (suis), Colon (suis), Duodenum (suis), Esophagus (suis), Eye (suis), Gallbladder (suis),","desc":"client-server","status":"Blue","date_due":"3/5/2018","date_created":"10/7/2018","imp":"Orange"},
{"task_id":59,"title":"ANTHOXANTHUM ODORATUM POLLEN, DACTYLIS GLOMERATA POLLEN, LOLIUM PERENNE POLLEN, PHLEUM PRATENSE POLLEN, and POA PRATENSIS POLLEN","desc":"De-engineered","status":"Maroon","date_due":"4/3/2018","date_created":"6/2/2018","imp":"Turquoise"},
{"task_id":60,"title":"Chlordiazepoxide Hydrochloride","desc":"groupware","status":"Mauv","date_due":"12/21/2018","date_created":"2/15/2019","imp":"Violet"},
{"task_id":70,"title":"Dicoria canescens","desc":"concept","status":"Teal","date_due":"6/2/2018","date_created":"7/21/2018","imp":"Orange"},
{"task_id":85,"title":"Bacillus subtilis","desc":"intermediate","status":"Mauv","date_due":"4/22/2018","date_created":"11/28/2018","imp":"Teal"}]

app = Flask(__name__)


@app.route('/')
def practice():
    return("<h1>Hello</h1><p>test</p>")


@app.route('/mock_data')
def api_all():
    return jsonify(mock_data)


@app.route('/api', methods= ['GET', 'POST'])
def index():
    if request.method == 'GET':
        dummy_json = {
                "test":"test"
                }
        return jsonify(dummy_data)
    
    if request.method == 'POST':
        response = request.values
        return jsonify(response)




@app.route('api2', methods = ['GET', 'POST'])
def prac():
    if request.method == 'POST':
        response = request.values.get('key')
        print(type(request.values))
        return jsonify({
                'data': response
                })


#@app.route('/tasks', methods=['GET', 'POST'])
#def view_tasks():
#
#    if request.method == 'GET':
#        tasks = return_all_tasks()
#        return render_template("tasks.html", tasks=tasks)
#
#    elif request.method == 'POST':
##        task_id = function to generate
#        title = request.form.get('name')
#        desc = request.form.get('desc', None)
##        status = function to set automatically
#        due_date = request.form.get('due_date', None)
##        date_created = function to generate
#        imp = request.form.get('imp')
    
##names are the ids for the input fields
    
#loop over objects
#return as dictionary
    

#@app.route('/tasks/id', methods=['GET', 'PUT', 'DELETE'])
#def task():
#    return render_template(f"tasks/{task_id}.html")
#    

    
if __name__ == '__main__':
    app.run(debug=True)



