class Product:
    def __init__(self, name, price, quantity):
        """Initialize the product with name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Display the information about the product."""
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Available Quantity: {self.quantity}")
    
    def update_quantity(self, quantity_change):
        """Update the quantity of the product (sold or restocked)."""
        self.quantity += quantity_change
        if self.quantity < 0:
            self.quantity = 0
        print(f"Updated Quantity for {self.name}: {self.quantity}")
    
    def get_value(self):
        """Calculate and return the value of this product in the inventory."""
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        """Initialize the inventory with an empty list of products."""
        self.products = []

    def add_product(self, name, price, quantity):
        """Add a new product to the inventory."""
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Product '{name}' added to the inventory.")

    def display_all_products(self):
        """Display all products in the inventory."""
        if self.products:
            print("\nInventory List:")
            for product in self.products:
                product.display_info()
                print("-" * 30)
        else:
            print("The inventory is empty.")

    def total_inventory_value(self):
        """Calculate and display the total value of the inventory."""
        total_value = sum(product.get_value() for product in self.products)
        print(f"\nTotal Inventory Value: ${total_value:.2f}")


# Simple scenario of using the system

def main():
    # Create the inventory system
    inventory = Inventory()
    
    # Add some products to the inventory
    inventory.add_product("Laptop", 1000.00, 10)
    inventory.add_product("Smartphone", 500.00, 25)
    inventory.add_product("Headphones", 150.00, 50)
    
    # Display all products in the inventory
    inventory.display_all_products()
    
    # Update quantity (sold and restocked)
    print("\nUpdating quantities:")
    inventory.products[0].update_quantity(-2)  # Sold 2 laptops
    inventory.products[1].update_quantity(10)  # Restocked 10 smartphones
    
    # Display updated inventory
    inventory.display_all_products()
    
    # Calculate and display total inventory value
    inventory.total_inventory_value()

if __name__ == "__main__":
    main()
