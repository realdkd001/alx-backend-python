import time
import sqlite3 
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection

#### paste your with_db_decorator here
""" your code goes here"""
def retry_on_failure(retries=3, delay=2):
    def outter(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1,retries+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt}: failed: {e}")
                    if attempt < retries:
                        print("Retrying...")
                        time.sleep(delay)
                    else:
                        print("All retry attempts failed.")
                        raise
            
        return wrapper
    return outter

@with_db_connection
@retry_on_failure(retries=4, delay=10)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)