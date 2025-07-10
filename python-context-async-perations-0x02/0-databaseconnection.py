import sqlite3
class DatabaseConnection:
    def __init__(self, db_url):
        self.db_url = db_url
        self.connection = None
        pass
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_url)
        print("✅ Database connection opened.")
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
        print("✅ Database connection closed.")
        

with DatabaseConnection("users.db") as cnx:
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())