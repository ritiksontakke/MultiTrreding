import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} second")

    time.sleep(seconds)

time1 = time.perf_counter()
# normal funtion
# func(4)
# func(3)

# threding funtion

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[3])

t1.start()
t2.start()

t1.join()
t2.join()

time2 = time.perf_counter()

print(time2 - time1)