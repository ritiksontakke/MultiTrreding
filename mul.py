# main.py

import threading
import multiprocessing
import pandas as pd
import time


# User Class
class User:

    def __init__(self, username, amount):
        self.username = username
        self.amount = amount

    def print_user(self):

        print(
            f"Username = {self.username}, "
            f"Amount = {self.amount}"
        )


# Thread Function
def thread_task(thread_name, file_name):

    # Read Excel File
    df = pd.read_excel(file_name)

    # Remove extra spaces from columns
    df.columns = df.columns.str.strip()

    # Loop all users
    for _, row in df.iterrows():

        # Create User Object
        user = User(
            row["username"],
            row["amount"]
        )

        # BEFORE UPDATE
        print(
            f"\nBEFORE {thread_name} -> "
            f"Username = {user.username} | "
            f"Amount = {user.amount} | "
            f"Memory = {id(user)}"
        )

        # Add +100
        user.amount += 100

        # AFTER UPDATE
        print(
            f"AFTER {thread_name}  -> "
            f"Username = {user.username} | "
            f"Amount = {user.amount} | "
            f"Memory = {id(user)}"
        )

        print("-" * 80)

        time.sleep(1)


# Process Function
def process_p1():

    print("\nPROCESS P1 STARTED\n")

    # Threads for 3 files
    t1 = threading.Thread(
        target=thread_task,
        args=("T1", "user_amounts_50000.xlsx")
    )

    t2 = threading.Thread(
        target=thread_task,
        args=("T2", "user_amounts_50000_file2.xlsx")
    )

    t3 = threading.Thread(
        target=thread_task,
        args=("T3", "user_amounts_50000_file3.xlsx")
    )

    # Start Threads Together
    t1.start()
    t2.start()
    t3.start()

    # Wait for all Threads
    t1.join()
    t2.join()
    t3.join()

    print("\nPROCESS P1 FINISHED")


# Main Program
if __name__ == "__main__":

    start_time = time.time()

    print("\nMAIN PROGRAM STARTED")

    # Create Process
    p1 = multiprocessing.Process(
        target=process_p1
    )

    # Start Process
    p1.start()

    # Wait Process
    p1.join()

    end_time = time.time()

    print("\nMAIN PROGRAM FINISHED")

    print(
        f"\nTOTAL EXECUTION TIME = "
        f"{end_time - start_time:.2f} seconds"
    )