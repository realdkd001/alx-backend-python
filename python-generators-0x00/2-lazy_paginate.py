seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(pagesize):
    offset = 0
    try:  
        while True:
            users = paginate_users(page_size=pagesize, offset=offset)
            if not users:
                break
            
            yield users
            offset += pagesize
            
    except Exception as e:
        print(f"Error: {e}")

    