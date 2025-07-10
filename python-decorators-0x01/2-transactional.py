import sqlite3 
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection

"""your code goes here"""
def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        cnx = args[0] if args else kwargs.get('conn')
        
        if cnx is None:
            raise ValueError("No database connection provided to the function.")

        try:
            result = func(*args, **kwargs)
            cnx.commit()
            print(f"Transaction committed: {func.__name__}()")
            return result
        except Exception as e:
            cnx.rollback()
            print(f"Transaction failed in {func.__name__}(): {e}. Rolled back.")
         
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')