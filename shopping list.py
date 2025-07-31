name =input("what is your name? ")
age = input("what is your age? ")
age = int(age)
age= age + 1
shopping= input("do you want to shop? (yes/no) ")
if shopping == "yes":
    print("please enter the number of items you want to buy: ")
else:
    print("please enter the item you would like to buy: ")
print("🛒 Welcome to Python Shop!")

# Ask how many items the user wants to buy
num_items = int(input("How many items would you like to buy? "))

# Create an empty list to store the items
shopping_cart = []

# Repeat for the number of items the user wants
for i in range(num_items):
    item = input(f"Enter the name of item {i+1}: ")
    shopping_cart.append(item)

# Display the shopping list
print("\n🧾 Your Shopping List:")
for item in shopping_cart:
    print("-", item)
print ("please enter the price of the item: ")
#create an empty list to store the price of the items in the shopping cart
shopping_cart_prices = []
# Repeat for the number of items the user wants
for i in range(num_items):
    price = float(input(f"Enter the price of item {i+1}: "))
    shopping_cart_prices.append(price)
# Calculate the total cost
total_cost = sum(shopping_cart_prices)
print(f"hello {name}, welcome to the system")
print(f"you are {age} years old")
print(f"the total cost of {shopping_cart} is {total_cost}")
#descrobing a comment
# this is a comment
print("nice having you here, welcome back {name}")

