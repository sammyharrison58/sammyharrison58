foods=[]
prices=[]
total=0.0
while True:
    food=input("Enter food item (q to quit): ")
    if food.lower()=='q':
        break
    else:
        price=float(input(f"Enter price of the {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
    total+=prices[i]
prices.sort()
print("---------------------")
print(f"Total: ${total:.2f}")

