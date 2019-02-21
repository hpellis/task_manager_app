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


@app.route('/api')
def api():
    x = Task()
    result = x.get_all_tasks()
    return jsonify(result)


@app.route('/', methods = ['GET', 'POST'])
def index():
    x = Task()
    if request.method == 'GET':
        result = x.call_api()
        return render_template('index.html', result=result)
    else:
        return "error"


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'GET':
        return render_template ('add_task.html')
    elif request.method == 'POST':
        x = Task()
        title = request.form.get('title')
        desc = request.form.get('desc')
        date_due = request.form.get('date_due')
        imp = request.form.get('imp')
        x.create_task(title, desc, date_due, imp)
        return redirect(url_for('index'))
    

@app.route('/task/<task_id>', methods = ['GET', 'POST'])
def update_task(task_id):
    return jsonify(task_id)



@app.route('/task/<task_id>', methods = ['GET', 'POST'])
def view_update_task(task_id):
    
    if request.method == 'GET':
        return render_template('task.html', task_id)
    
    if request.method == 'PUT':
        x = Task()
        title = request.form.get('title')
        desc = request.form.get('desc')
        date_due = request.form.get('date_due')
        imp = request.form.get('imp')
        x.update_task(title, desc, date_due, imp)
        return redirect(url_for('index'))
        
    if request.method == 'DELETE':
        x = Task()
        x.delete_task(task_id)
        return redirect(url_for('index'))
        
        
       
        

#def filter_by_id():
#    sql_statement = "SELECT * FROM to_do_list WHERE id = {}".format(id)
#    results = sql_statement.results
#    return jsonify(results)
#         
#@app.route('/api/task/<task_id>', methods = ['GET'])
#def single_task():
#    x = Task()
#    if request.method == 'GET':
#        result = x.query(''' SELECT * FROM tasks WHERE task_id = {} ''').format(task_id)
#        return jsonify(result)
    
      
#@app.route('/api/task/<task_id>/update', methods = ['PUT'])
#def update_task():
#    x = Task()
#    
#    if request.method == 'PUT':
#        
#        task_id = request.form.get('update_task_id')
#        title = request.form.get('update_title')
#        desc = request.form.get('update_desc')
#        date_due = request.form.get('update_date_due')
#        imp = request.form.get('update_imp')
#
#        x.update_task(task_id, title, desc, date_due, imp)
#        
#        pass

        
 


if __name__ == '__main__':
    app.run(debug=True)


