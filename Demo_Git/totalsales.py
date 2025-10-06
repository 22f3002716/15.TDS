import json

# Step 1: Load the JSON file
with open("sales.json", "r") as f:
    data = json.load(f)

# Step 2: Read the 'total_sales' value (stored as a hex string)
hex_value = data["total_sales"]

# Step 3: Convert from hexadecimal (base 16) to decimal (base 10)
total_sales = int(hex_value, 16)

# Step 4: Print the decoded result
print("Total sales:", total_sales)