menu = {
    "pizza": 99,
    "burger": 49,
    "pasta": 50,
    "pepsi": 45,
    "cake": 30,
    "ice cream": 25
}

# greet
print("Welcome to your Restaurant")
print("Here is the menu:")
print("Pizza: Rs-99\nBurger: Rs-49\nPasta: Rs-50\nPepsi: Rs-45\nCake: Rs-30\nIce Cream: Rs-25")

order_total = 0

while True:
    item = input("Enter the item you want to order (or type 'no' to finish): ").lower()
    
    if item == "no":
        break
    
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item.title()} has been added to the order.")
    else:
        print(f"Sorry, we don't have {item.title()} on the menu.")

print(f"\nThe total amount for your order is Rs-{order_total}.")
