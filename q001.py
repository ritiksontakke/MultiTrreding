import threading

def task():
    print("hello world")

t= threading.Thread(target=task)

t.start()
t.join()