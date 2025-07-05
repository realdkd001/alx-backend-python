from contextlib import closing
seed = __import__('seed')


def stream_users_in_batches(batch_size):
    try:
        with closing(seed.connect_to_prodev()) as cnx:
            with closing(cnx.cursor(dictionary=True)) as cursor:
                cursor.execute("SELECT * FROM user_data;")
                
                while True:
                    batch = cursor.fetchmany(int(batch_size))
                    if not batch:
                        break
                    yield batch   
                        
    except Exception as e:
        print(f"Error: {e}")

def batch_processing(batch_size):
    try:
        for batch in stream_users_in_batches(batch_size=batch_size):
            filtered_users = filter(lambda user: user['age'] > 25, batch)
            for user in filtered_users:
                print(user)
                return user
            
    except Exception as e:
        print(f"Error: {e}")