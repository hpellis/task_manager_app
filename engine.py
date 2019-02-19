#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:41:13 2019

@author: harriet
"""
from datetime import datetime
from os.path import exists
from sqlite3 import connect

class Task():
    
    def __init__(self):
        
        self.db_path = 'static/database/tasks.db'
        
#        self.task_id = task_id
#        self.title = title
#        self.desc = desc
#        self.status = status
#        self.due_date = due_date
#        self.date_created = datetime.now()
#        self.imp = imp
     
        
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
            query = "SELECT * from tasks;"
            self.query(query)
            return self.results
        except Exception as e:
            print(e)
        
        
    def create_task(self, task_id, title, desc=None, due_date):
        self.task_id = task_id
        self.title = title
        self.desc = desc
#        but optional?
        self.status = "to do"
        self.due_date = due_date
        self.date_created = datetime.now()
        self.imp = imp
        
    def update_task(self):
        pass
        
    def complete_task(self):
        pass
    
#    def create_task(self):

#        
        
x = Task()

result = x.get_all_tasks()

print(result)
    
#self.creation_date = datetime.now()
    
    
#needed functionality:
#   function to get all tasks
#    return_all_tasks()
#    function to add a task
#    create_task()
#    
#    
#    
#    
#    
