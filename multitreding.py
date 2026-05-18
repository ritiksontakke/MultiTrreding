import threading

import time

start = time.perf_counter()

def do_someting():
    print("Sleeping 1 sec")
    time.sleep(1)
    print("Done slepping")

t1 = threading.Thread(target=do_someting)
t2 = threading.Thread(target=do_someting)

t1.start()
t2.start()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2 )} second(2)")