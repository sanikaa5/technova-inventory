# app.py

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

if __name__ == "__main__":
    print("Welcome to Inventory Management System")
    inv = Inventory()
    inv.add_item("Shoes")
    inv.add_item("Sandals")
    print("Current Inventory:", inv.get_items())
