# main.py

import time
import threading
import multiprocessing


class User:
    id: int
    name: str
    amount: int

    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount

    def print_user(self, process_name):
        return (
            f"process/thread: {process_name} "
            f"id: {self.id}, "
            f"name: {self.name}, "
            f"amount: {self.amount}"
        )


def thread_task(process_name, user):

    # update shared object
    user.amount += 100

def process_task(process_name, user):

    # one thread inside process
    t1 = threading.Thread(
        target=thread_task,
        args=(process_name, user)
    )

    t1.start()
    t1.join()

    print(
        f"{process_name} AFTER PROCESS -> "
        f"user memory location = {id(user)}, "
        f"user : {user.print_user(process_name)}"
    )


if __name__ == "__main__":

    start_time = time.time()

    # Create user in MAIN PROCESS
    user = User(1, "Pratik", 100)

    print(
        f"MAIN PROCESS -> "
        f"user memory location = {id(user)}, "
        f"user : {user.print_user('MAIN')}"
    )

    processes = []

    # create processes
    for i in range(1, 6):

        process_name = f"P{i}"

        p = multiprocessing.Process(
            target=process_task,
            args=(process_name, user)
        )

        processes.append(p)

    # start processes
    for p in processes:
        p.start()

    # wait for processes
    for p in processes:
        p.join()

    print(
        f"\nMAIN PROCESS END -> "
        f"user memory location = {id(user)}, "
        f"user : {user.print_user('MAIN')}"
    )

    print(
        f"\nMain program finished. "
        f"total_time_taken: {time.time() - start_time:.2f} seconds\n"
    )
# deep copy

"""
MAIN PROCESS -> user memory location = 2243415913008, user : process/thread: MAIN id: 1, name: Pratik, amount: 100
P1 AFTER PROCESS -> user memory location = 2295944121712, user : process/thread: P1 id: 1, name: Pratik, amount: 200
P2 AFTER PROCESS -> user memory location = 2938327862640, user : process/thread: P2 id: 1, name: Pratik, amount: 200
P3 AFTER PROCESS -> user memory location = 1453485919600, user : process/thread: P3 id: 1, name: Pratik, amount: 200
P4 AFTER PROCESS -> user memory location = 2523779960176, user : process/thread: P4 id: 1, name: Pratik, amount: 200
P5 AFTER PROCESS -> user memory location = 3104078695792, user : process/thread: P5 id: 1, name: Pratik, amount: 200

MAIN PROCESS END -> user memory location = 2243415913008, user : process/thread: MAIN id: 1, name: Pratik, amount: 100

Main program finished. total_time_taken: 0.33 seconds
"""