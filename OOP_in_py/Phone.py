from items import Item


#child class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # call to super function to have access to all attributes/ methods of the parent class
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Number of broken phones {broken_phones} should be cannot be < 0"
        self.broken_phones = broken_phones



