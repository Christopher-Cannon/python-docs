# Warehouse class
class warehouse:
    def __init__(self, initial_stock):
        self.stock = initial_stock

    # Add a stock item and quantity
    def add_stock(self, key, value):
        self.stock[key] = value

        print("Added {}: {}".format(key, value))

    # Remove a stock item
    def remove_stock(self, key):
        del self.stock[key]

        print("Removed {}".format(key))

    # Return a single stock item
    def return_item(self, key):
        return self.stock[key]

    # Return the entire dictionary
    def return_all_items(self):
        return self.stock

# Create a new instance of a warehouse class
edi = warehouse({"Apples": 10, "Oranges": 12, "Lemons": 7, "Bananas": 18})

# Add pears to the stock list
edi.add_stock("Pears", 28)

# Remove apples from the stock list
edi.remove_stock("Apples")

lemons = edi.return_item("Lemons")

print("Lemons:", lemons)

# Get the stock list and print out everything
all_stock = edi.return_all_items()

for key, value in all_stock.items():
    print("\n{}: {}".format(key, value))
