class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hello {self.name}")

p = Person("Vinny")
p.say_hi()
