# main.py

import time
import threading
import multiprocessing
import pandas as pd


# User Class
class User:

    def __init__(self, username, amount):
        self.username = username
        self.amount = amount

    def print_user(self, process_name, thread_name):

        return (
            f"process: {process_name} | "
            f"thread: {thread_name} | "
            f"username: {self.username} | "
            f"amount: {self.amount}"
        )


# Thread Function
def thread_task(process_name, thread_name, file_name):

    # Read Excel File
    df = pd.read_excel(file_name)

    # Remove spaces from columns
    df.columns = df.columns.str.strip()

    # Loop Users
    for _, row in df.iterrows():

        # Create User Object
        user = User(
            row["username"],
            row["amount"]
        )

        # BEFORE UPDATE
        print(
            f"\n{process_name} {thread_name} BEFORE -> "
            f"user memory location = {id(user)}, "
            f"user : "
            f"{user.print_user(process_name, thread_name)}"
        )

        # Add +100
        user.amount += 100

        # AFTER UPDATE
        print(
            f"{process_name} {thread_name} AFTER -> "
            f"user memory location = {id(user)}, "
            f"user : "
            f"{user.print_user(process_name, thread_name)}"
        )

        print("-" * 80)

        time.sleep(1)


# Process Function
def process_task(process_name, thread_name, file_name):

    print(f"\n{process_name} STARTED")

    # One Thread Inside One Process
    t1 = threading.Thread(
        target=thread_task,
        args=(process_name, thread_name, file_name)
    )

    t1.start()
    t1.join()

    print(f"\n{process_name} FINISHED")


# Main
if __name__ == "__main__":

    start_time = time.time()

    print("\nMAIN PROGRAM STARTED\n")

    processes = []

    # Process + Thread + File Mapping
    tasks = [
        ("P1", "T1", "user_amounts_50000.xlsx"),
        ("P2", "T2", "user_amounts_50000_file2.xlsx"),
        ("P3", "T3", "user_amounts_50000_file3.xlsx")
    ]

    # Create Processes
    for process_name, thread_name, file_name in tasks:

        p = multiprocessing.Process(
            target=process_task,
            args=(process_name, thread_name, file_name)
        )

        processes.append(p)

    # Start Processes
    for p in processes:
        p.start()

    # Wait Processes
    for p in processes:
        p.join()

    print("\nMAIN PROGRAM FINISHED")

    print(
        f"\nTOTAL EXECUTION TIME = "
        f"{time.time() - start_time:.2f} seconds\n"
    )