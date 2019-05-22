'''
-------------------------------------------------------------------------------
Name:		cash_bonus_in_class.py
Purpose:	tells you the about of cash bonus you get depending on the class average for mid-term and finals

Author:	Cho.J

Created:	date in 25/03/2019
------------------------------------------------------------------------------
'''

#GET the mid term and the final class average
mid_term = float(input("What is the class average for midterm? "))
finals = float(input("What is the class average for the finals? "))

#COMPUTE the difference and find how much the children improved from before and after
average = finals - mid_term

#CHECK what the bonus cash will be depending on the average
if average > 0.1:
    print("Congratulations, the cash bonus is $600! ")

elif average > 0:
    print("Congratulations, the cash bonus is $100")

elif average < 0:
    print("Sorry, there is no cash bonus for you")

else:
    print("The cash bonus is $300")
