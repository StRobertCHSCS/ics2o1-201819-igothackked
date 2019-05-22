

exchange_rate = float(input("Enter the Canadian to US dollar exchange rate: "))
start = int(input("Enter the starting value: "))
end = int(input("Enter the end value: "))
can_price = 0
us_price = 0

print("")
print("Canada price ---> US price")
for i in range(start, end + 1, 10):
   can_price = can_price + 10
   us_price = exchange_rate*can_price
   print(can_price, "----->", us_price)


