
talk = input("Is the parrot talking? ")
time = int(input("What is the current hour? "))

if talk == "yes" and time>7 and time<20:
    print("Everything is fine")

elif talk == "no":
    print("Everything is fine")
else:
    print("We're in trouble!")

