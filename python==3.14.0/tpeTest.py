from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5]

#Created a thread pool with three threads that will be used to concurrently
#execute the print_number function onto the list passed to it
with ThreadPoolExecutor(max_workers = 3) as executor:
    results = executor.map(print_number, numbers)

#Because we are working with multiple threads we can get the output relatively 
#quickly
for result in results:
    print(result)