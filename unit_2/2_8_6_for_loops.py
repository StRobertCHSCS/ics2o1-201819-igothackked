
numbers = int(input("amount of numbers: "))
total = 0

for i in range(1, numbers + 1, 1):
    total_number = int(input("Enter a number "))
    total = total_number + total

print("sum:", total)