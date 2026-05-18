import threading
import time

from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"slepping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def poolingDemo():
    with ThreadPoolExecutor() as excutors:
        # futures = excutors.submit(func, 3)
        # print(futures.result())
        # futures = excutors.submit(func, 2)
        # print(futures.result())
        # futures = excutors.submit(func, 1)
        # print(futures.result())

        l = [3,5,6,7]

        results = excutors.map(func, l)
        for result in results:
            print(result)

poolingDemo()