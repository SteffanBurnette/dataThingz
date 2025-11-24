class Guy:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age #Private variable

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, val):
        self.__name = val

    def set_age(self, val):
        self.__age = val

guy = Guy("Steffan", 23)
#Will not work and will throw an error
#print(guy.__name)

print(guy.get_name())
print(guy.get_age())

#This will still work to get direct access to the values