#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:41:13 2019

@author: harriet
"""

from flask import Flask, request, render_template, jsonify
#from flask_cors import CORS
import json
import sqlite3
from engine import Task

mock_data=[{"task_id":37,"title":"sorbitol","desc":"Cross-group","status":"Fuscia","date_due":"3/26/2018","date_created":"10/25/2018","imp":"Mauv"},
{"task_id":46,"title":"Buspirone hydrochloride","desc":"Face to face","status":"Goldenrod","date_due":"8/10/2018","date_created":"7/22/2018","imp":"Orange"},
{"task_id":64,"title":"Topiramate","desc":"bottom-line","status":"Aquamarine","date_due":"10/27/2018","date_created":"5/30/2018","imp":"Green"},
{"task_id":73,"title":"Titanium Dioxide","desc":"client-server","status":"Red","date_due":"5/23/2018","date_created":"8/27/2018","imp":"Fuscia"},]

app = Flask(__name__)


@app.route('/')
def practice():
    return("<h1>Hello</h1><p>test</p>")


@app.route('/mock_data')
def mock_data():
    return jsonify(mock_data)

#this one limits what gets jsonified
#this is our api that gets task
@app.route("/api/task/<int:id>>", methods = ['GET', 'POST'])
def task_single(id):
    if request.method == 'GET'
        sql_statement = "SELECT * FROM tasks WHERE id = {} ".format(id)
    #    c.execute(sql_statement, id)
        return jsonfiy({"task":results})
    
    if request.method == 'POST':
        pass

#this is api that gets all tasks    
@app.route("/api/tasks", methods = ['GET'])
def all_tasks(id):
    if request.method == 'GET'
        sql_statement = "SELECT * FROM tasks WHERE id = {} ".format(id)
    #    c.execute(sql_statement, id)
        return jsonfiy({"task":results})
    
    if request.method == 'POST':
        pass
    
       


@app.route('/tasks')
def api_get_all_tasks():
    x = Task()
    result= x.get_all_tasks()
    return jsonify(result)


@app.route('/tasks/<task_id>', methods = ['GET', 'POST'])
def get_xxxx(task_id):
    if request.method == 'GET':
        return jsonify(tasks.read(xxxx))
    
    
@app.route('/tasks/add', methods = ['POST'])
def create_task():
    if request.method == 'POST':
        data = request.json
        title = data.get('title')
        desc = data.get('desc', None)
        
        if not title:
            pass
    
#@app.route('tasks/<task_id>', methods = ['PUT'])       
#def update_task(task_id):
#    pass
#    
#
#@app.route('tasks/<task_id>'), methods = ['DELETE']
#def delete_task(task_id):
#    pass
#    






#@app.route('/tasks', methods=['POST'])
#def create():
#    if request.method == 'POST':
#        data = request.json
#        title = data.get('title', None)
#        description = data.get('description', None)
#
#        if not title or not description:
#            return "The fields 'title' and 'description' are required", 400
#
#        task = tasks_dao.create(data)
#
#        return jsonify(task), 201
    
    
#loop over objects
#return as dictionary
    

#@app.route('/addtask', methods = ['GET', 'POST'])
#def create_task():
#    x = Task()
#    task_id = request.form.get('task_id')
#    title = request.form.get('title')
#    desc = request.form.get('title')
#    due_date = request.form.get('title')
#    create_task(task_id, title, desc, due_date)
    


#    def create_task(self, task_id, title, desc=None, due_date):
#        self.task_id = task_id
#        self.title = title
#        self.desc = desc
##        but optional?
#        self.status = "to do"
#        self.due_date = due_date
#        self.date_created = datetime.now()
#        self.imp = imp
#            

#
#@app.route('/api', methods= ['GET', 'POST'])
#def index():
#    if request.method == 'GET':
#        dummy_json = {
#                "test":"test"
#                }
#        return jsonify(dummy_data)
#    
#    if request.method == 'POST':
#        response = request.values
#        return jsonify(response)




#@app.route('api2', methods = ['GET', 'POST'])
#def prac():
#    if request.method == 'POST':
#        response = request.values.get('key')
#        print(type(request.values))
##        create dictionary of 
#        return jsonify({
#                'data': response
#                })


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
    

    

#@app.route('/tasks/id', methods=['GET', 'PUT', 'DELETE'])
#def task():
#    pass
#    


#@app.route('/api/task/add', methods = 'POST')
#def add_task():
#    x = Task()
#    
#    if request.method == 'POST':
#        data = request.json
#        title = data.get('title')
#        desc = data.get('desc')
#        date_due = data.get('date_due')
#        imp = data.get('imp')
#        
#        x.create_task(title, desc, date_due, imp)
#        
#        return "successfully added task"
#    
#    else:
#        pass
    
if __name__ == '__main__':
    app.run(debug=True)



