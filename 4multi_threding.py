import time
import asyncio
import httpx
from functools import wraps

POST_URL = "https://jsonplaceholder.typicode.com/posts"
USERS_URL = "https://jsonplaceholder.typicode.com/users"
COMMENT_URL = "https://jsonplaceholder.typicode.com/comments"
COUNTRIES_URL = "https://restcountries.com/v3.1/alpha/IN"

def time_it(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
    return wrapper

async def fetch_posts(client):
    res = await client.get(POST_URL)
    a=0
    for _ in range(10000):
        a = a+(10*20/60+1+9*64**32*66/346**755)
    return res

async def fetch_users(client):
    res = await client.get(USERS_URL)
    a=0
    for _ in range(10000):
        a = a+(10*20/60+1+9*64**32*66/346**755)
    return res

async def fetch_comments(client):
    res = await client.get(COMMENT_URL)
    a=0
    for _ in range(10000):
        a = a+(10*20/60+1+9*64**32*66/346**755)
    return res

async def fetch_counters(client):
    res = await client.get(COUNTRIES_URL)
    a=0
    for _ in range(10000):
        a = a+(10*20/60+1+9*64**32*66/346**755)
    return res

@time_it
async def main():
    async with httpx.AsyncClient(timeout=200) as client:
        task = []

        for _ in range(10):
            task.append(
                asyncio.gather(
                    fetch_posts(client),
                    fetch_comments(client),
                    fetch_counters(client),
                    fetch_users(client)
                )
            )

        await asyncio.gather(*task)

if __name__ == "__main__":
    asyncio.run(main())
