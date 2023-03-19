import concurrent.futures

# Define a function that simulates a long-running CPU-bound task


def do_work(x):
    result = 0
    for i in range(x):
        result += i
    return result


# Define a list of inputs to the do_work function
inputs = [5000000, 10000000, 15000000, 20000000]

# Create a ThreadPoolExecutor with 2 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit the do_work function with each input to the executor
    futures = [executor.submit(do_work, x) for x in inputs]

    # Wait for all the futures to complete
    results = [f.result() for f in concurrent.futures.as_completed(futures)]

# Print the results
print(results)
