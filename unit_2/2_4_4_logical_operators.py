
#Given 2 ints, output True if
# one if them is 10 or if their
# sum is 10, otherwise output False.

print ("input two numbers, if they add up to 10 or are 10 it will print True, if not it will print False")
one = int(input("What is the first number? "))
two = int(input("What is the second number? "))

if one + two == 10:
    print("True")
elif one == 10 or two == 10:
    print("True")
else:
    print("False")