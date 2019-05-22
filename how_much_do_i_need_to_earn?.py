


#ADD in how much money i spend pre month

want = float(input("Enter the amount of money you want: "))
have = float(input("Enter the amount of money you have: "))
spend = float(input(("Enter the amount of money you spend per month: ")))
time_you_want_it_by = int(input("Enter when you want this amount of money in (years): "))


months = time_you_want_it_by*12
total_need = want - have
total = total_need//months


print("you will need to make $", str(total + spend), "per month to get to $" + str(want), "in", str(time_you_want_it_by), "years")