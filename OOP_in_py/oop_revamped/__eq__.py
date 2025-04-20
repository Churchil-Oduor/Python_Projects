# __eq__() is used for comparison

# Create a class

class Person:
    def __init__(self, name, _id):
        self.name = name
        self.id = _id

    def __eq__(self, other_person):
        if self.name == other_person.name and self.id == other_person.id:
            return (f"Same Person")
        return (f"Different People")

person_list = [Person("Churchil", 4672579), Person("Hope", 678269)]
print(person_list[0].__eq__(person_list[0]))
