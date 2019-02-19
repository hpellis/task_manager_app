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
            
    
    def create_task(self, task_id, title, desc, date_due, imp):
        self.task_id = task_id
        self.title = title
        self.desc = desc
        self.status = 'to do'
        self.date_due = date_due
        self.date_created = datetime.now()
        self.imp = imp
        
        try:
            self.connect_db()
            query = ''' INSERT INTO tasks(task_id, title, desc, status, date_due, date_created, imp)
            VALUES(?,?,?,?,?,?,?)''' (self.task_id, self.title, self.desc, self.status, self.date_due, self.date_created, self.imp)
            self.c.execute(query)
            self.c.commit()
            self.connection.close()
            
        except Exception as e:
            print(e)
            
x = Task()

#result = x.get_all_tasks()    

x.create_task(4, 'doctor appointment', 'book appointment', '20/03/2019', 1)   
        
        
#    def update_task(self):
##        need SQL statement here
#        pass
            
#    def delete_task(self):
#        need SQL statement here
#        pass
