from concurrent.futures import ProcessPoolExecutor
import time

def square_number(num):
    time.sleep(1)
    return f"Squared: {num**2}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Needed when performing parrallelism 
if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers = 3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)