class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("Initializing {} ...".format(self.name))

        Robot.population += 1

    def die(self):
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))
        
    def say_hi(self):
        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots".format(cls.population))


droid1 = Robot("Vin")
droid1.say_hi()
droid2 = Robot("Chacho")
droid1.how_many()
droid2.die()
droid2.say_hi()

