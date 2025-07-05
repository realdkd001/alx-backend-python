import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os
import uuid
import csv

load_dotenv()
port = int(os.getenv("PORT")) 
db_host = os.getenv("HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("PASSWORD")
database = "ALX_prodev"

def connect_db():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            port=port
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return connection

def create_database(connection):
    if connection is None:
        raise RuntimeError("No Connection to Database")
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
        cursor.close()
        print(f"Database {database} created or already exists.")
    except mysql.connector.Error as err:
        print("Failed creating database:", err)


def connect_to_prodev():
    try:
        
        return mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            port=port,
            database=database
        )
    except mysql.connector.Error as err:
        if err.errno  in (errorcode.ER_BAD_DB_ERROR,  errorcode.ER_NO_DB_ERROR):
            cnx = connect_db()
            create_database(cnx)
            cnx.close()
        else:
            print(f"Error connecting to {database}:", err)
        return None


def create_table(connection):
    if connection is None:
        print("No Connection to Database")
        return

    cursor = connection.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(150) NOT NULL,
                email VARCHAR(200) NOT NULL,
                age DECIMAL NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE INDEX idx_user_data ON user_data(user_id)
        ''')
        print("Table and index created.")
    except mysql.connector.Error as err:
        print("Error creating table:", err)


def insert_data(connection=None, data=None):
    if connection is None:
        print("No connection to the database.")
        return
    
    if data is None:
        print("No filepath provided")
        return
    
    users = read_users_stream(data)
    cursor = connection.cursor()
    
    try:
        for user in users:
            cursor.execute('''
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            ''', user)
        connection.commit()
        cursor.close()
        print("Streaming insert completed successfully.")
    except mysql.connector.Error as err:
        print("Error inserting data:", err)
        
        
def read_users_stream(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield (
                    str(uuid.uuid4()),
                    row['name'],
                    row['email'],
                    float(row['age'])
                )