class  Animals:
    class Human:
        def __init__(self, name, age):
            self.name = name;
            self.age = age;

        def details(self):
            return (f"My name is {self.name} and I am {self.age} yrs old")

    class fish:
        def __init__(self, name, age):
            self.name = name;
            self.age = age;

        def details(self):
            return (f"Hello I am a {self.name} and I am {self.age}")

person = Animals.Human("Chacho", 22)
fish = Animals.fish("catfish", 34)

print(person.details())
print(fish.details())
