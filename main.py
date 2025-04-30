import json

#Step 1: Read the dictionary from expenses.json
with open('expenses.json', 'r') as file:
        expenses = json.load(file)

#Step 2: Add up the total price for all the expenses at the "pet store"
pet_store_total = sum(item["price"] for item in expenses.get("pet store", [] ) )

print(pet_store_total)

# read `expenses.json`

# get and print total "price" for all expenses at the "pet store"


