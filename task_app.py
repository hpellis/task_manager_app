#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:17:14 2019

@author: harriet
"""

from flask import Flask, request, render_template, jsonify
import json
import sqlite3
from engine import Task

app = Flask(__name__)

@app.route('/api/tasks', methods = ['GET'])
def get_all_tasks():
    x = Task()
    if request.method == 'GET':
        result = x.get_all_tasks()
        return jsonify(result)
    else:
#        something here
        pass
    

@app.route('/api/task/<task_id>', methods = ['GET', 'POST'])
def single_task():
    x = Task()
    
    if request.method == 'GET':
        result = 





@app.route("/api/task/<int:id>>", methods = ['GET', 'POST'])
def task_single(id):
    if request.method == 'GET'
        sql_statement = "SELECT * FROM tasks WHERE id = {} ".format(id)
    #    c.execute(sql_statement, id)
        return jsonfiy({"task":results})
    
    if request.method == 'POST':
        pass
    

if __name__ == '__main__':
    app.run(debug=True)


