
string = input("Enter a string: ")
total = 0

for i in range (len(string)):
    if string[i] == "c" and string[i + 1] == "o" and string[i +3] == "e":
        total = total + 1

print(total)