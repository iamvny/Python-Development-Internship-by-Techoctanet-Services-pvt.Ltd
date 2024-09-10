# Receipt Calculator in Python (Indian Currency)

# Define a function to add items to the receipt
def add_item():
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter the price of {item_name} (in ₹): "))
            quantity = int(input(f"Enter the quantity of {item_name}: "))
            items.append({'name': item_name, 'price': price, 'quantity': quantity})
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")
    
    return items

# Define a function to calculate total and generate the receipt
def calculate_total(items, tax_rate=0.05):
    subtotal = 0
    for item in items:
        item_total = item['price'] * item['quantity']
        subtotal += item_total
        print(f"{item['name']} x{item['quantity']}: ₹{item_total:.2f}")
    
    tax = subtotal * tax_rate
    total = subtotal + tax
    print("\nSubtotal: ₹{:.2f}".format(subtotal))
    print(f"Tax ({tax_rate * 100}%): ₹{tax:.2f}")
    print("Total: ₹{:.2f}".format(total))

# Main program
def receipt_calculator():
    print("Welcome to the Receipt Calculator!")
    items = add_item()
    tax_rate = float(input("Enter tax rate (e.g., 0.05 for 5%): ") or 0.05)
    calculate_total(items, tax_rate)

# Run the calculator
receipt_calculator()
