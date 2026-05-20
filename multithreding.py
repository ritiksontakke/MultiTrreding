# main.py

import threading
import multiprocessing
import time

class User:
    id: int
    name: str
    amount: int

    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount

    def print_user(self):
        print(f"id: {self. id}, name: {self.name}, amount: {self.amount}")

def thread_task(thread_name, a):
    for i in range(3):
        print(f"before sum {thread_name} -> a = {a}")
        a = a+1
        print(f"{thread_name} -> a = {a}")
        print(f"{thread_name} -> memory location of a = {id(a)}")

        time.sleep(1)


def process_p1():
    print("Process P1 started")
    
    user = User(1, "Pratik", 1000)

    print(f"p1 start -> a = {a}")
    print(f"p1 start -> memory location of a = {id(a)}")

    # Create threads
    t1 = threading.Thread(target=thread_task, args=("T1", a))
    t2 = threading.Thread(target=thread_task, args=("T2", a))
    t3 = threading.Thread(target=thread_task, args=("T3", a))

    # Start threads
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()


    print(f"p1 end -> a = {a}")
    print(f"p1 end -> memory location of a = {id(a)}")

    print("Process P1 finished")


if __name__ == "__main__":

    # Create process P1
    p1 = multiprocessing.Process(target=process_p1)

    # Start process
    p1.start()

    # Wait for process to finish
    p1.join()

    print("Main program finished")


"""
case 1:

Process P1 started
p1 start -> a = 0
p1 start -> memory location of a = 140722165347416

before sum T1 -> a = 0
T1 -> a = 1
T1 -> memory location of a = 140722165347448

before sum T2 -> a = 0
T2 -> a = 1
T2 -> memory location of a = 140722165347448

before sum T3 -> a = 0
T3 -> a = 1
T3 -> memory location of a = 140722165347448

p1 end -> a = 0
p1 end -> memory location of a = 140722165347416
Process P1 finished
Main program finished
"""

"""
Process P1 started
p1 start -> a = 0
p1 start -> memory location of a = 140722165347416

before sum T1 -> a = 0
T1 -> a = 1
T1 -> memory location of a = 140722165347448

before sum T1 -> a = 1
T1 -> a = 2
T1 -> memory location of a = 140722165347480

before sum T1 -> a = 2
T1 -> a = 3
T1 -> memory location of a = 140722165347512


before sum T2 -> a = 0
T2 -> a = 1
T2 -> memory location of a = 140722165347448

before sum T2 -> a = 1
T2 -> a = 2
T2 -> memory location of a = 140722165347480

before sum T2 -> a = 2
T2 -> a = 3
T2 -> memory location of a = 140722165347512


before sum T3 -> a = 0
T3 -> a = 1
T3 -> memory location of a = 140722165347448

before sum T3 -> a = 1
T3 -> a = 2
T3 -> memory location of a = 140722165347480

before sum T3 -> a = 2
T3 -> a = 3
T3 -> memory location of a = 140722165347512


p1 end -> a = 0
p1 end -> memory location of a = 140722165347416
Process P1 finished
Main program finished
"""