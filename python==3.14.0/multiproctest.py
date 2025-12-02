import multiprocessing
import time

"""
The main goal is to execute the two functions in sepereate processes to achieve
parallel processing.

Both of the process will have their own seperate memory
"""

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"The original value: {i}, the Squared value: {i**2}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"The original value: {i}, the Cubed Value: {i**3}")

if __name__ == "__main__":
    # Creating the two processes
    p1 = multiprocessing.Process(target = square_numbers)
    p2 = multiprocessing.Process(target = cube_numbers)

    #Starting the processes
    t = time.time()
    p1.start()
    p2.start()

    #Waiting for the processes to finish
    p1.join()
    p2.join()
    finished = time.time() - t

    print(f"Time taken to execute parrallel processes: {finished}")