# main.py

import time
import threading
import multiprocessing


def thread_task(process_name, user):

    # shared update
    user["amount"] += 100

    print(
        f"{process_name} -> "
        f"user memory = {id(user)} "
        f"user = {dict(user)}"
    )


def process_task(process_name, user):

    t1 = threading.Thread(
        target=thread_task,
        args=(process_name, user)
    )

    t1.start()
    t1.join()

    print(
        f"{process_name} AFTER PROCESS -> "
        f"user memory = {id(user)} "
        f"user = {dict(user)}"
    )


if __name__ == "__main__":

    start_time = time.time()

    # Shared manager
    manager = multiprocessing.Manager()

    # ONE shared object
    user = manager.dict({
        "id": 1,
        "name": "Pratik",
        "amount": 100
    })

    print(
        f"MAIN START -> "
        f"user memory = {id(user)} "
        f"user = {dict(user)}"
    )

    processes = []

    for i in range(1, 100001):

        process_name = f"P{i}"

        p = multiprocessing.Process(
            target=process_task,
            args=(process_name, user)
        )

        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join()

    print(
        f"\nMAIN END -> "
        f"user memory = {id(user)} "
        f"user = {dict(user)}"
    )

    print(
        f"\nTotal time: {time.time() - start_time:.2f} sec"
    )

    """
MAIN START -> user memory = 2425973083840 user = {'id': 1, 'name': 'Pratik', 'amount': 100}
P1 -> user memory = 2371254108912 user = {'id': 1, 'name': 'Pratik', 'amount': 200}
P1 AFTER PROCESS -> user memory = 2371254108912 user = {'id': 1, 'name': 'Pratik', 'amount': 200}
P3 -> user memory = 2705538237168 user = {'id': 1, 'name': 'Pratik', 'amount': 300}
P3 AFTER PROCESS -> user memory = 2705538237168 user = {'id': 1, 'name': 'Pratik', 'amount': 300}
P2 -> user memory = 2843141554928 user = {'id': 1, 'name': 'Pratik', 'amount': 400}
P2 AFTER PROCESS -> user memory = 2843141554928 user = {'id': 1, 'name': 'Pratik', 'amount': 500}
P5 -> user memory = 1978881426160 user = {'id': 1, 'name': 'Pratik', 'amount': 500}
P4 -> user memory = 3126774612720 user = {'id': 1, 'name': 'Pratik', 'amount': 600}
P5 AFTER PROCESS -> user memory = 1978881426160 user = {'id': 1, 'name': 'Pratik', 'amount': 600}
P4 AFTER PROCESS -> user memory = 3126774612720 user = {'id': 1, 'name': 'Pratik', 'amount': 600}

MAIN END -> user memory = 2425973083840 user = {'id': 1, 'name': 'Pratik', 'amount': 600}
"""