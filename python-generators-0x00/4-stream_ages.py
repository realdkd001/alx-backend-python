from contextlib import closing
seed = __import__('seed')

def stream_user_ages():
    with closing(seed.connect_to_prodev()) as cnx:
        with closing(cnx.cursor(dictionary=True)) as cursor:
            cursor.execute("SELECT age FROM user_data;")
            for row in cursor:
                yield row

def calculate_average_age():
    total_age = 0
    total_user = 0
    for user in stream_user_ages():
        total_age += user["age"]
        total_user += 1
        
    average = total_age / total_user if total_user > 0 else 0
    
    print(f"Average age of users: {average}")

calculate_average_age()