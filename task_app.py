#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:17:14 2019

@author: harriet
"""

from flask import Flask, request, render_template, jsonify, redirect, url_for
import json
import sqlite3
from engine import Task

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='GET':
        api_results = call_api()
        return render_template('index.html', api_results = api_results)
    elif request.method =='POST':
        print('post request on api?')
        return None

#@app.route('/')
#def index():
#    tasks_to_show = retrieve_tasks()
#    return render_template('index.html', tasks_to_show = tasks_to_show)

@app.route('/api')
def api():
    tasks_to_show = retrieve_tasks()
    return tasks_to_show

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method =='GET':
        return render_template("index.html")
    elif request.method =='POST':
        form_data = request.form
        task_name = form_data['a-task']
        create_task(task_name)
        return redirect(url_for('index'))
    
    
    
    


@app.route('/api/tasks', methods = ['GET'])
def get_all_tasks():
    x = Task()
    if request.method == 'GET':
        result = x.get_all_tasks()
        return jsonify(result)
    else:
        pass    


@app.route('/api/task/<task_id>', methods = ['GET'])
def single_task():
    x = Task()
    if request.method == 'GET':
        result = x.query(''' SELECT * FROM tasks WHERE task_id = {} ''').format(task_id)
        return jsonify(result)
    
#above are the two apis that call from front end pages
#make GET requests to these 

    

@app.route('/')
def home():
    

    
    
@app.route('/api/task/add', methods = 'POST')
def add_task():
    x = Task()
    
    if request.method == 'POST':

        title = request.form.get('title')
        desc = request.form.get('desc')
        date_due = request.form.get('date_due')
        imp = request.form.get('imp')

        x.create_task(title, desc, date_due, imp)
        
        return render_template('')
    
    else:
        pass        
         



   
    
        
@app.route('/api/task/<task_id>/update', methods = ['PUT'])
def update_task():
    x = Task()
    
    if request.method == 'PUT':
        
        task_id = request.form.get('update_task_id')
        title = request.form.get('update_title')
        desc = request.form.get('update_desc')
        date_due = request.form.get('update_date_due')
        imp = request.form.get('update_imp')

        x.update_task(task_id, title, desc, date_due, imp)
        
        pass
    
#@app.route('/api/task/<task_id>/delete', methods = ['DELETE'])
#def delete_task():
#    x = Task()
#    
#    task_id = <task_id>
#    
#    if request.method == 'DELETE':
#        x.delete_task(task_id)
#    

        
        


        




if __name__ == '__main__':
    app.run(debug=True)


