#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:41:13 2019

@author: harriet
"""
from datetime import datetime
from os.path import exists
from sqlite3 import connect
import json
import requests

class Task():
    
    def __init__(self):
        self.db_path = 'static/database/tasks.db'
         
    def check_db(self):
        if exists(self.db_path):
            return True
        else:
            return False
    
    def connect_db(self):
        if self.check_db():
            try:
                self.connection = connect(self.db_path)
                self.c = self.connection.cursor()
            except Exception as e:
                print(e)
        else:
            print('Database path does not exist.')  

    def query(self, query):
        try:
            self.connect_db()
            self.c.execute(query)
            self.results = self.c.fetchall()
            self.connection.close()
            return self.results
        except Exception as e:
            print(e)

    def get_all_tasks(self):
        try:
            query = "SELECT * from tasks ORDER BY date_due ASC;"
            self.query(query)
            return self.results
        except Exception as e:
            print(e)     
    
    def create_task(self, title, desc, date_due, imp):
        self.title = title
        self.desc = desc
        self.status = 'to do'
        self.date = date_due
        format_date = '%Y-%m-%d'
        self.date_due = datetime.strptime(self.date, format_date)
        self.date_created = datetime.now()
        self.imp = imp
        try:
            self.connect_db()
            query = ''' INSERT INTO tasks(title, desc, status, date_due, date_created, imp)
            VALUES(?, ?, ?, ?, ?, ?)''' 
            self.c.execute(query, (self.title, self.desc, self.status, self.date_due, self.date_created, self.imp))
            self.connection.commit()
            self.c.close()
        except Exception as e:
            print(e)

    def delete_task(self, task_id):
        self.task_id = task_id
        try:
            self.connect_db()
            query = ''' DELETE FROM tasks WHERE task_id = ? '''
            self.c.execute(query, self.task_id)
            self.connection.commit()
            self.c.close()
        except Exception as e:
            print(e)

    def update_task(self, task_id, title, desc, status, date_due, imp):
        self.task_id = task_id
        self.title = title
        self.desc = desc
        self.status = status
        self.date_due = date_due
        self.imp = imp
        try:
            self.connect_db()
            query = ''' UPDATE tasks SET title=?, desc=?, status=?, date_due=?, imp=? WHERE task_id=? '''
            self.c.execute(query, (self.title, self.desc, self.status, self.date_due, self.imp, self.task_id))
            self.connection.commit()
            self.c.close() 
        except Exception as e:
            print(e)       
            
    def call_api(self):
        try:
            endpoint = 'http://127.0.0.1:5000/api'
            response = requests.get(endpoint)
            if response.status_code == 200:
                data = response.json()
                return data
            elif response.status_code == 400:
                print("400")
            elif response.status_code == 500:
                print("error 500") 
        except:
            print("Error with API")
                

x = Task()

#x.create_task('doctor appointment', 'book appointment', '20/03/2019', "1")  
#
#x.create_task('buy groceries', 'buy groceries for party', '10/03/2019', "0")  

#x.create_task('shops', 'go to shops', '19/03/2019', "0")  

    
#x = Task()
#    
##result = x.get_all_tasks()    
#
##x.create_task(4, 'doctor appointment', 'book appointment', '20/03/2019', 1)   
#
##x.delete_task("4")
#
#x.update_task("4", "Doctor Appt", "book appt ASAP", "in progress", "20/04/2019", 1)
#     
         