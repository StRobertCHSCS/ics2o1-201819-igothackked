
word = input("Enter a string: ")
total = 0

for i in range(len(word)):
    if word[i] == "h" and word[1+i] == "i":
        total = total + 1

print("there are", total, "Hi's")