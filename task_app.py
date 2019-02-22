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


@app.route('/delete/<task_id>', methods=['POST', 'GET'])
def delete_task(task_id):
    if request.method == 'POST':
        x = Task()
        x.delete_task(task_id)
        return redirect(url_for('confirm_delete'))


@app.route('/delete/confirm', methods = ['GET'])
def confirm_delete():
    return render_template('delete_confirm.html')


@app.route('/update/<task_id>', methods = ['GET', 'POST'])
def update_task(task_id):
    x = Task()
    task_id = task_id
    if request.method == 'GET':
        result = x.call_api()
        for item in result:
            if item[0] == int(task_id):
                specific_item=item
        return render_template('update.html', specific_item=specific_item, task_id=task_id)
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')
        status = request.form.get('status')
        date_due = request.form.get('date_due')
        imp = request.form.get('imp')
        x.update_task(task_id, title, desc, status, date_due, imp)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


