import time
import io
import httpx
from functools import wraps
import threading

POST_URL = "https://jsonplaceholder.typicode.com/posts"
USERS_URL = "https://jsonplaceholder.typicode.com/users"
COMMENT_URL = "https://jsonplaceholder.typicode.com/comments"
COUNTRIES_URL = "https://restcountries.com/v3.1/alpha/IN"

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
    return wrapper

def fetch_posts():
    res = httpx.get(POST_URL)
    a=0
    for _ in range(10000):
        a = a+(10*20/60+1+9*64**32*66/346**755)
    return res

def fetch_users():
    res = httpx.get(USERS_URL)
    a=0
    for _ in range(10000):
        a = a+(10*20/60+1+9*64**32*66/346**755)
    return res

def fetch_comments():
    res = httpx.get(COMMENT_URL)
    a=0
    for _ in range(10000):
        a = a+(10*20/60+1+9*64**32*66/346**755)
    return res

def fetch_counters():
    res = httpx.get(COUNTRIES_URL)
    a=0
    for _ in range(10000):
        a = a+(10*20/60+1+9*64**32*66/346**755)
    return res

@time_it
def main():
    threads = []
         

    for _ in range(10):
        t1 = threading.Thread(target=fetch_posts, name="fetch_posts")
        t2 = threading.Thread(target=fetch_users, name="fetch_users")
        t3 = threading.Thread(target=fetch_comments, name="fetch_comments")
        t4 = threading.Thread(target=fetch_counters, name="fetch_counters")

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        threads.extend([t1, t2, t3])
    
    for threads in threads:
        threads.join()


if __name__ == "__main__":
    main()