import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = args[0] if args else kwargs.get('query',"")
        with open("query.log", "a") as file:
            file.write(f"[{datetime.now()}] Query: {query}\n")
        return func(*args, **kwargs)
    return wrapper
        
     

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.commit() 
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
