# main.py
import time
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

    def print_user(self, thread_name):
        return (f"thread_name/proccess: {thread_name} id: {self.id}, name: {self.name}, amount: {self.amount}")


def thread_task(thread_name, user):
    user.amount += 100

    print(f"{thread_name} -> user memory location = {id(user)}, user : {user.print_user(thread_name)}")

def process_p1():

    print("Process P1 started\n")

    user = User(1, "Pratik", 100)

    print("P1 START")
    user.print_user("P1")
    print(f"P1 -> user memory location = {id(user)} user : {user.print_user("P1")}\n")

    threads = []

    for i in range(1, 100001):

        thread_name = f"T{i}"

        t = threading.Thread(
            target=thread_task,
            args=(thread_name, user)
        )

        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    print("\nP1 END")
    user.print_user("P1")
    print(f"P1 -> user memory location = {id(user)} user : {user.print_user("P1")}\n")

    print("Process P1 finished")


if __name__ == "__main__":
    start_time = time.time()

    p1 = multiprocessing.Process(target=process_p1)

    p1.start()
    p1.join()

    print(f"\nMain program finished. total_time_taken:{time.time()-start_time:.2f} seconds \n")

"""
Process P1 started

P1 START
P1 -> user memory location = 2324192276704 user : thread_name/proccess: P1 id: 1, name: Pratik, amount: 100

T1 -> user memory location = 2324192276704, user : thread_name/proccess: T1 id: 1, name: Pratik, amount: 200
T2 -> user memory location = 2324192276704, user : thread_name/proccess: T2 id: 1, name: Pratik, amount: 300
T3 -> user memory location = 2324192276704, user : thread_name/proccess: T3 id: 1, name: Pratik, amount: 400

P1 END
P1 -> user memory location = 2324192276704 user : thread_name/proccess: P1 id: 1, name: Pratik, amount: 400

Process P1 finished
"""