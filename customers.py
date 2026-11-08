
# Lucas Camargo Morschel
# ISM2411 - Python for Business
# November 8, 2026
# Lab 11 - Customer Dictionary & Lookup

# Reflection 1:
# I would use .get() when I'm not sure if a customer has certain
# information saved in their record. If I know the information
# is there, I would just use brackets to access it.

# Reflection 2:
# Exercise 8 reminded me of how Excel can organize sales
# information and calculate totals for different regions.
# Python might be better for bigger amounts of data because
# it can do those calculations automatically and save time.


# Exercise 1 - One Customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2 - Update and Add

# Add a phone number
customer["phone"] = "555-1234"
print("After adding phone:", customer)

# Update the tier to platinum
customer["tier"] = "platinum"
print("After updating tier:", customer)

# Delete the email field
del customer["email"]
print("After deleting email:", customer)


# Exercise 3 - Safe Lookup

# Safely look up the deleted email
email = customer.get("email", "no email on file")
print("Safe lookup:", email)

# Try bracket notation and catch the KeyError
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# Exercise 4 - Iterate Through Dictionary

# Loop using .items() to get both keys and values
for key, value in customer.items():
    print(f"{key}: {value}")

# Loop without .items() to get only the keys
for key in customer:
    print(key)

# Without .items(), the loop returns only the dictionary keys.
# With .items(), it returns both the keys and their values.


# Exercise 5 - Lookup Table

# Create the discount lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

# Find the customer's discount rate
discount_rate = tier_discounts.get(customer["tier"], 0)

# Calculate the final price of a $200 purchase
purchase_amount = 200
final_price = purchase_amount * (1 - discount_rate)

# Print the results
print("Tier:", customer["tier"])
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")


# Exercise 6 - List of Dictionaries

# Create three customer records
customers = [
    {"name": "Bob", "tier": "bronze"},
    {"name": "Carol", "tier": "silver"},
    {"name": "David", "tier": "gold"}
]

# Calculate each customer's discount on a $300 purchase
for person in customers:
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{person['name']} ({tier}): ${discount_amount:.2f} discount")


# Exercise 7 - Nested Product Catalog

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

# Check each product's stock
for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {details['stock']} left")


# Exercise 8 - Sales by Region

# Create a list of transactions
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

# Create an empty summary dictionary
sales_by_region = {}

# Add up sales for each region
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

# Print totals sorted alphabetically by region
for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
