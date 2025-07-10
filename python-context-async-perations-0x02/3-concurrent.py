import aiosqlite
import asyncio

db_url = "users.db"

async def async_fetch_users():
    async with aiosqlite.connect(db_url) as cnx:
            async with cnx.execute("SELECT * FROM users") as cursor:
                users = await cursor.fetchall()
                print("All users:", users)
                return users
            
async def async_fetch_older_users():
    async with aiosqlite.connect(db_url) as cnx:
        async with cnx.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            older_users = await cursor.fetchall()
            print("Users older than 40:", older_users)
            return older_users


async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(), 
        async_fetch_older_users()
        )
    
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())