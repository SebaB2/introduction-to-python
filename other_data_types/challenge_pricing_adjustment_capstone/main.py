grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

eggs = grocery_inventory.get("Eggs")
eggs_price = eggs[1]
if eggs_price > 5:
    eggs_price = eggs_price-1
    grocery_inventory["Eggs"] = (grocery_inventory["Eggs"][0],eggs_price, grocery_inventory["Milk"][2] )
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of eggs is reasonable")

#Adding tomatos
grocery_inventory.update({"Tomatoes":("Produce", 1.2, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)

#Managing stock
milk = grocery_inventory.get("Milk")
milk_stock = milk[2]
if milk_stock < 10:
    milk_stock = milk_stock + 20
    grocery_inventory["Milk"] = (grocery_inventory["Milk"][0],grocery_inventory["Milk"][1],milk_stock)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    

else:
    print("Milk has sufficent stock")

#Remove item based on price
apples = grocery_inventory.get("Apples")
apples_price = apples[1]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

#Final print
print("Updated inventory: ", grocery_inventory)