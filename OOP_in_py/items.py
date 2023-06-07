import csv


# Parent Class
class Item:
    pay_rate = 0.8 # class attribute
    all = []
    # constraining the type of name and price entered by the user
    def __init__(self, name: str, price: float, quantity = 0):
        # make sure that the price and quantity are >= 0 by using assert statement
        assert price >= 0, f"Price {price} is not greater than or equal to zero" #setting an assertion error that alerts the user after wrong inputs
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    # this decorator makes the name READ-ONLY and creates a behaviour of getter as that of java and C#
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    # This decorator allows the setting of the name attribute to another value i.e enables the setter trait
    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception("Length entered is too long")
        else:
            self.__name = new_name

    def view_item(self):
        return (f"This is a {self.name}\n Price {self.price}\n Quantity {self.quantity}\n")

    def apply_discount(self):
        self.__price = self.pay_rate * self.__price
    


    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)


#child class
#class Phone(Item):
#   def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # call to super function to have access to all attributes/ methods of the parent class
#        super().__init__(name, price, quantity)
#       assert broken_phones >= 0, f"Number of broken phones {broken_phones} should be cannot be < 0"
#       self.broken_phones = broken_phones


#print(Phone("iphone", 30000, 12, 4).view_item())
 


