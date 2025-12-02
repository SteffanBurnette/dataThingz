import threading
import time

"""
Will create threads to handle concurrent execution, when one function is asleep
the program will execute the other function and vise versa
"""
def print_numbers():
    for i in range(10):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for x in "ABCDEFGHIJ":
        time.sleep(2)
        print(f"Letter: {x}")


#creating threads
t1 = threading.Thread(target = print_numbers) #This thread is responsible for executing the numbers function
t2 = threading.Thread(target = print_letters) # This thread is respoinsible for the executing the letters function

t = time.time()
#Strating the thread
#Starting the thread is essentially executing the code block that said thread is
#responsible for when the resources become avaliable. Because is am making the 
#function's iteration sleep right before each logic statement, the order of
#what is executing will alternate between the function that is not sleeping 
#at that time
t1.start()
t2.start()

#Wait for the thread to be complete
t1.join()
t2.join()
finished_time = time.time() - t
print(f"Time taken to execute: {finished_time}")