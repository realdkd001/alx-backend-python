import time
import sqlite3 
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection

query_cache = {}

"""your code goes here"""
def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        query = kwargs.get("query")
        if query is None and len(args) > 1:
            query = args[1]

        if not query:
            raise ValueError("Query string is missing or invalid")
                
        key = f"{func.__name__}:{query.strip().lower()}"
        cached_query = query_cache.get(key)
        result = None
        if cached_query is not None:
            print("Using cached result.")
            result = cached_query
        else:
            try: 
                result = func(*args, **kwargs)
                query_cache[key] = result
                print("Result cached.")
            except Exception as e:
                print(f"Error while executing {func.__name__}(): {e}")
                raise
        print(result)
        return result
    
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")