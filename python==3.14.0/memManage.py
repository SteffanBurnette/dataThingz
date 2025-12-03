import gc

class MyObject:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} deleted")

## Creating a circular reference
# Its best practice to try an avoid having circular references like this in
# your code
obj1 = MyObject("obj1")
obj2 = MyObject("obj2")
obj1.ref = obj2
obj2.ref = obj1

# Handling circulare reference
del obj1
del obj2

#Will need to manually trigger the garabage collection since they still
## reference eachother due to the circular reference
gc.collect()

print(f"Garbage collected objects: {gc.garbage}")