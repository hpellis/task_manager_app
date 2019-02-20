#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:46:24 2019

@author: harriet
"""

import sqlite3

def connect_database():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    return conn, cursor


def create_table():
    conn, cursor = connect_database()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (task_id INTEGER PRIMARY KEY, title TEXT, desc TEXT, status TEXT, date_due TEXT, date_created TEXT, imp TEXT)')
    conn.close()

create_table()