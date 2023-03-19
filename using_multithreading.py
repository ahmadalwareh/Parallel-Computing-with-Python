import os
import threading
import time

counter = [0]


def task_sleep(sleep_duration, task_number, lock, counter):
    # ock.acquire()
    with lock:
        counter[0] += 1
        # Perform operation that require a common data/resource
        # lock.release()
        print(counter[0])
        time.sleep(sleep_duration)
        print(f"Task {task_number} done (slept for {sleep_duration}s)! "
              f"Main thread: {threading.main_thread().name}, "
              f"Current thread: {threading.current_thread().name}, "
              f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    time_start = time.time()

    # Create lock (optional)
    thread_lock = threading.Lock()

    # Create thread
    t1 = threading.Thread(target=task_sleep, args=(2, 1, thread_lock, counter))
    t2 = threading.Thread(target=task_sleep, args=(2, 2, thread_lock, counter))
    t3 = threading.Thread(target=task_sleep, args=(2, 3, thread_lock, counter))

    # Start task execution
    t1.start()
    t2.start()
    t3.start()

    # Wait for thread to complete execution
    t1.join()
    t2.join()
    t3.join()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")
