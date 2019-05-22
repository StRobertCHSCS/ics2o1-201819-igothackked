
total_days = 0
total_spent = 0

daily_spend = int(input("Enter a daily pent amount (-1 to stop): "))
total_spent = total_spent + daily_spend
while daily_spend != -1:
    daily_spend = int(input("Enter a daily pent amount (-1 to stop): "))
    total_spent = float(total_spent + daily_spend)
    total_days = total_days + 1

print("Total days traveled:", total_days)
print("total amount spent $" + str(total_spent + 1))

if 250<total_spent/total_days:
    print("you owe a fee of $" + str((total_spent + 1)*.13))

else:
    print("Phew you dont have a fee to pay")