
# ISM2411 - Lab 11
# Customer Dictionary & Lookup

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
