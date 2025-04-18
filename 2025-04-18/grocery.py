# Create dictionary named inventory with items and price 
inventory = {
    'Apple': 150.5,
    'Milk': 28.9,
    'Bread': 40.2,
    'Cheese': 65.0,
    'Banana': 62.6,
    'Onion': 22.3,
    'Tomato': 16.5,
}

print(inventory)

# Create a list named cart with selected item names 
cart= ['Onion','Bread','Orange','Onion','Cheese']

# Print data types using type()
print("Data Types:")
print(f"Type of inventory: {type(inventory)}")
print(f"Type of a price value: {type(inventory['Milk'])}")
print(f"Type of cart: {type(cart)}")
print()

# Calculate total bill using a for loop and check item availability
total_bill = 0.0
print("Checking Cart Items:")
for item in cart:
    if item in inventory:
        price = inventory[item]
        total_bill += price
        print(f"{item.title()} is available at ${price}")
    else:
        print(f"Warning: {item.title()} is not available in inventory.")

# Convert cart list into a set to show only unique items
unique_items = set(cart)
print(f"\nUnique items in cart: {unique_items}")
print(f"Type of unique_items: {type(unique_items)}")

# Create a tuple of product categories
categories = ("Fruits", "Dairy", "Bakery","Vegetables")
print(f"\nProduct Categories: {categories}")

#Add an item with None as its price ahow its type
inventory['Cucumber']=None
print(f"\nCucumber price is:  {inventory['Cucumber']}")
print(f"Type of Cucumber price is:  {type(inventory['Cucumber'])}")

# Apply discount logic using a boolean
is_discount_applied = False
if total_bill > 100:
    is_discount_applied = True
    total_bill *= 0.95  # Apply 5% discount

    
print(f"\nIs discount applied? {is_discount_applied}, Type: {type(is_discount_applied)}")
print(f"Total Bill: ${total_bill}")
