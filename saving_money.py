


money_now = float(input("Enter the amount of money you have right now: "))
need = float(input("Enter the amount of money you need to save up to: "))
income = float(input("Enter the amount of money you receive per month: "))
money_gone = float(input("Enter the amount of money you typically spend per month: "))


total_need = need - money_now
total_gain = income - money_gone
months_needed = total_need//total_gain
 
year_needed = months_needed//12
remainder_of_months_after_years = months_needed%12
print("you will need", int(year_needed), "years and", int(remainder_of_months_after_years), "months to have $" + str(need),)

