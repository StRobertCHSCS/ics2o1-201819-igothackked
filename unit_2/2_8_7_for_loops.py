
total = 0
number_of_times = int(input("How many products are there: "))

for i in range(1, number_of_times + 1, 1):
    price = float(input("please enter the price of the product: "))
    amount = int(input("please enter the quantity of the product: "))
    total = total + (price*amount)

total_cost = (total*0.13) + total

print("the total today will be $" + str(round(total_cost, 2),))