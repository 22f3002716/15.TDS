# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
# ]
# ///
# print("Hello World")
# print("Welcome to Git")
# print("This is a demo file for Git")
# print("This file is named abc.py")
# print("This file is located in Demo_Git folder")
# print("This is the last line of the file")
# print("This file is named abc.py")
# print("This file is located in Demo_Git folder")
# print("This is the last line of the file")


import json

# Input JSON array (paste your 100-item array here)
data = [{"category":"Home","price":142.15,"name":"Pro Gadget"},{"category":"Books","price":55.4,"name":"Mini Set"},{"category":"Toys","price":34.13,"name":"Super Kit"},{"category":"Apparel","price":191.02,"name":"Ultra Gadget"},{"category":"Apparel","price":123.77,"name":"Pro Item"},{"category":"Toys","price":148.55,"name":"Pro Tool"},{"category":"Home","price":34,"name":"Smart Tool"},{"category":"Books","price":125.87,"name":"Eco Device"},{"category":"Books","price":85.89,"name":"Eco Device"},{"category":"Toys","price":62.02,"name":"Deluxe Kit"},{"category":"Electronics","price":41.14,"name":"Mini Kit"},{"category":"Toys","price":58.4,"name":"Eco Item"},{"category":"Electronics","price":43.02,"name":"Smart Widget"},{"category":"Books","price":170.98,"name":"Super Widget"},{"category":"Apparel","price":81.21,"name":"Super Widget"},{"category":"Home","price":183.62,"name":"Deluxe Tool"},{"category":"Electronics","price":167.88,"name":"Deluxe Gadget"},{"category":"Home","price":198.13,"name":"Smart Tool"},{"category":"Apparel","price":29.3,"name":"Super Item"},{"category":"Books","price":170.1,"name":"Eco Kit"},{"category":"Books","price":187.27,"name":"Super Widget"},{"category":"Apparel","price":127.33,"name":"Mini Widget"},{"category":"Electronics","price":36.37,"name":"Deluxe Item"},{"category":"Books","price":119.48,"name":"Mini Item"},{"category":"Apparel","price":97.18,"name":"Deluxe Item"},{"category":"Home","price":63.16,"name":"Super Item"},{"category":"Toys","price":103.73,"name":"Smart Kit"},{"category":"Electronics","price":53.06,"name":"Deluxe Item"},{"category":"Electronics","price":21.29,"name":"Pro Tool"},{"category":"Books","price":73.35,"name":"Ultra Set"},{"category":"Books","price":143.41,"name":"Mini Set"},{"category":"Apparel","price":126.49,"name":"Smart Widget"},{"category":"Electronics","price":64.71,"name":"Deluxe Gadget"},{"category":"Toys","price":150.06,"name":"Mini Tool"},{"category":"Toys","price":20.8,"name":"Eco Tool"},{"category":"Home","price":81.84,"name":"Ultra Widget"},{"category":"Electronics","price":76.57,"name":"Eco Device"},{"category":"Books","price":198.78,"name":"Pro Tool"},{"category":"Electronics","price":170.29,"name":"Ultra Tool"},{"category":"Books","price":109.36,"name":"Mini Tool"},{"category":"Books","price":74.67,"name":"Ultra Tool"},{"category":"Home","price":32.93,"name":"Ultra Device"},{"category":"Home","price":49.08,"name":"Super Gadget"},{"category":"Books","price":127.49,"name":"Mini Kit"},{"category":"Toys","price":99.26,"name":"Smart Kit"},{"category":"Books","price":186.64,"name":"Mini Widget"},{"category":"Books","price":58.06,"name":"Ultra Widget"},{"category":"Toys","price":130.27,"name":"Pro Item"},{"category":"Toys","price":165.23,"name":"Mini Gadget"},{"category":"Home","price":55.72,"name":"Ultra Tool"},{"category":"Toys","price":84.07,"name":"Smart Gadget"},{"category":"Books","price":73.79,"name":"Smart Kit"},{"category":"Books","price":110.16,"name":"Ultra Item"},{"category":"Toys","price":147.11,"name":"Mini Kit"},{"category":"Apparel","price":97.55,"name":"Mini Set"},{"category":"Home","price":113.07,"name":"Eco Set"},{"category":"Home","price":173.08,"name":"Deluxe Set"},{"category":"Toys","price":103.46,"name":"Ultra Set"},{"category":"Apparel","price":39.53,"name":"Deluxe Device"},{"category":"Electronics","price":192.57,"name":"Eco Kit"},{"category":"Toys","price":169.04,"name":"Mini Device"},{"category":"Toys","price":137.66,"name":"Deluxe Device"},{"category":"Apparel","price":152.44,"name":"Pro Item"},{"category":"Home","price":199.4,"name":"Pro Device"},{"category":"Books","price":42.31,"name":"Deluxe Kit"},{"category":"Toys","price":98.47,"name":"Smart Item"},{"category":"Apparel","price":126.99,"name":"Deluxe Set"},{"category":"Electronics","price":180.34,"name":"Deluxe Tool"},{"category":"Home","price":72.7,"name":"Deluxe Tool"},{"category":"Books","price":194.08,"name":"Pro Device"},{"category":"Books","price":136.53,"name":"Mini Widget"},{"category":"Electronics","price":150.26,"name":"Deluxe Device"},{"category":"Books","price":25.31,"name":"Deluxe Gadget"},{"category":"Books","price":22.89,"name":"Ultra Tool"},{"category":"Electronics","price":110.69,"name":"Mini Set"},{"category":"Apparel","price":35.22,"name":"Eco Set"},{"category":"Apparel","price":47.8,"name":"Pro Kit"},{"category":"Books","price":189.14,"name":"Pro Device"},{"category":"Books","price":54.93,"name":"Super Kit"},{"category":"Toys","price":146.95,"name":"Super Item"},{"category":"Toys","price":100.67,"name":"Eco Set"},{"category":"Apparel","price":92.84,"name":"Mini Gadget"},{"category":"Home","price":118.27,"name":"Mini Tool"},{"category":"Apparel","price":175.64,"name":"Mini Kit"},{"category":"Home","price":82.65,"name":"Eco Item"},{"category":"Toys","price":34.67,"name":"Smart Kit"},{"category":"Home","price":88.12,"name":"Ultra Widget"},{"category":"Apparel","price":62.41,"name":"Eco Tool"},{"category":"Apparel","price":187.9,"name":"Mini Set"},{"category":"Books","price":32.04,"name":"Deluxe Set"},{"category":"Books","price":32.72,"name":"Smart Tool"},{"category":"Apparel","price":69.3,"name":"Deluxe Gadget"},{"category":"Electronics","price":93.06,"name":"Mini Item"},{"category":"Apparel","price":151.64,"name":"Ultra Item"},{"category":"Apparel","price":81.09,"name":"Smart Widget"},{"category":"Books","price":39.98,"name":"Pro Kit"},{"category":"Books","price":156.82,"name":"Eco Tool"},{"category":"Electronics","price":148.63,"name":"Eco Set"},{"category":"Apparel","price":174.99,"name":"Eco Gadget"},{"category":"Electronics","price":160.76,"name":"Mini Item"}]
# 1️⃣ Filter out items with price < 81.33
filtered = [item for item in data if item["price"] >= 81.33]

# 2️⃣ Sort by category (A→Z), price (high→low), then name (A→Z)
sorted_items = sorted(
    filtered,
    key=lambda x: (x["category"], -x["price"], x["name"])
)

# 3️⃣ Output as minified JSON (no spaces or newlines)
minified_json = json.dumps(sorted_items, separators=(',', ':'))

print(minified_json)