# __str__() method enables the creation of a string from an object

# create a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name}  {self.age}")


print(Person("Churchil", 12))

