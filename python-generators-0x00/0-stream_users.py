from contextlib import closing
seed = __import__('seed')

def stream_users():
    try:
        with closing(seed.connect_to_prodev()) as cnx:
            with closing(cnx.cursor(dictionary=True)) as cursor:
                cursor.execute("SELECT * FROM user_data;")
                for row in cursor:
                    yield row
    except:
        pass