"""
Will be splitting up the factorial calculation process to multiple CPU cores
to reduce the execution time.
"""

import multiprocessing
import math
import sys
import time

#Setting the maximum number of digits that we can work with for integer conversion
sys.set_int_max_str_digits(100000)

#Function to compute factorial of a given number
def factorial(n):
    if n <= 0:
        return 1
    
    return n * factorial(n - 1)

print(factorial(3))

#Using the math library to compute the factorial
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

## Needed when performing parallism
if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]  

    start = time.time()

    #Creating a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time Taken: {end_time - start} seconds")
    