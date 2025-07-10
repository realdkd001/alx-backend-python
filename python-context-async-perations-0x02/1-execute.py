import sqlite3
class ExecuteQuery:
    def __init__(self, query, parameters=None):
        self.query = query
        self.parameters = parameters or ()
        if parameters is not None and not isinstance(parameters, (tuple, list)):
            parameters = (parameters,)
        self.connection = None
        self.db_url = "users.db"
        
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_url)
        print("Database connection opened.")
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.query, self.parameters)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Error: {e}")
            raise
            
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
        print("Database connection closed.")
        
with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as result:
    print (result)