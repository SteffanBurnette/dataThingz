"""
This file will contain examples of ustilizing generators to write
memory efficient code.
"""

# Created a generator that outputs numbers in a given range
def generate_nums(n):
    for i in range(n):
        yield i

# Using the generator
for num in generate_nums(100000):
    print(num)
    if num > 10:
        break