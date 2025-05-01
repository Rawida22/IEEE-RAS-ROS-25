class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __add__(self,item,quantity):
        self.items[item] = quantity

    def __remove__(self,item):
        return self.items.pop(item)
    
    def __Total__(self):
        return sum(self.items.values())
    def __display__(self):
        for item , quantity in self.items.items():
            print(f"{item} - {quantity}")
   
cart1= ShoppingCart()
cart1.__add__("Papaya", 100)
cart1.__add__("Guava",200)
cart1.__add__("Orange",150)
print(f"Current Items in Cart: ")
cart1.__display__()
print(f"Total Quantity: {cart1.__Total__()}\n")

print(f"Updated Items in Cart after removing Orange:")
cart1.__remove__("Orange")
cart1.__display__()
print(f"Total Quantity: {cart1.__Total__()}")

