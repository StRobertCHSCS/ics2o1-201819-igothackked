
string = input("enter a string: ")
cat_total = 0
dog_total = 0
true_false = False

for i in range(len(string)):
    if string[i] == "c" and string[i +1] == "a" and string[i + 2] == "t":
        cat_total = cat_total + 1
    if string[i] == "d" and string[i+1] == "o" and string[i+2] == "g":
        dog_total = dog_total + 1
    if dog_total == cat_total:
        true_false = True

print(true_false)

kjbk 'ou' \
     '' \
     'u'
kjb