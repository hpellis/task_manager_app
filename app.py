#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:41:13 2019

@author: harriet
"""

from flask import Flask, render_template, request
from engine import ToDo

app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template("layout.html")



@app.route('/')
def practice():
    return"<h1>Hello</h1><p>test</p>"


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
#        
#        
#        
#        
##names are the ids for the input fields
#
#@app.route('/tasks/id', methods=['GET', 'PUT', 'DELETE'])
#def task():
#    return render_template(f"tasks/{task_id}.html")
#    

    
if __name__ == '__main__':
    app.run(debug=True)
