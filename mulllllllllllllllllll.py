# main.py

import time
import threading
import pandas as pd


# User Class
class User:

    def __init__(self, username, amount):
        self.username = username
        self.amount = amount

    def print_user(self, thread_name):

        return (
            f"thread: {thread_name} | "
            f"username: {self.username} | "
            f"amount: {self.amount}"
        )


# Thread Function
def thread_task(thread_name, file_name):

    # Read Excel File
    df = pd.read_excel(file_name)

    # Remove spaces from columns
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
            f"\n{thread_name} BEFORE -> "
            f"user memory location = {id(user)}, "
            f"user : {user.print_user(thread_name)}"
        )

        # Update Amount
        user.amount += 100

        # AFTER UPDATE
        print(
            f"{thread_name} AFTER -> "
            f"user memory location = {id(user)}, "
            f"user : {user.print_user(thread_name)}"
        )

        print("-" * 80)


if __name__ == "__main__":

    start_time = time.time()

    print("\nMAIN THREAD STARTED\n")

    threads = []

    # Thread + File Mapping
    tasks = [
        ("T1", "user_amounts_50000.xlsx"),
        ("T2", "user_amounts_50000_file2.xlsx"),
        ("T3", "user_amounts_50000_file3.xlsx")
    ]

    # Create Threads
    for thread_name, file_name in tasks:

        t = threading.Thread(
            target=thread_task,
            args=(thread_name, file_name)
        )

        threads.append(t)

    # Start Threads
    for t in threads:
        t.start()

    # Wait Threads
    for t in threads:
        t.join()

    print("\nMAIN THREAD FINISHED")

    print(
        f"\nMain program finished. "
        f"total_time_taken: "
        f"{time.time() - start_time:.2f} seconds\n"
    )