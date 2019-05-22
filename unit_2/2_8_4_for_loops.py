
start = int(input("Enter first number "))
end = int(input("Enter the last number: "))
total = 0
big_number = 0

if start>end:
    for i in range(start, end + 1, 1):
        total = total + 1
        print(total)

else:
    for m in range(start, end + 1, -1):
        big_number = big_number + 1
        print(big_number)
