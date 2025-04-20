
# Creating a class customer that holds customer details

class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city


list_of_customers = [Customer("Hope", "Las Vegas"), Customer("Victor", "Texas")]

print(list_of_customers[0].name)
