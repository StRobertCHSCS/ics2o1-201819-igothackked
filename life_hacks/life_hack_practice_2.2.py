
'''
-------------------------------------------------------------------------------
Name:		vacation_this_summer?.py
Purpose:	tells you f you parents will let you go on vacation this summer

Author:	Cho.J

Created:	date in 19/03/2019
------------------------------------------------------------------------------
'''

#GET your final average and how much you saved up
average = int(input("What is your average?: "))
money = int(input("How much did you save up?: "))

#CHECK if you are going to europe, california or just staying home this summer
if average>=80 and money>= 500:
    print("CONGRATULATIONS YOU ARE GOING TO EUROPE THIS SUMMER!!!")

elif average>=80:
    print("YAY! you can go to California!")

else:
    print("You will stay home studying in your room the whole summer :)")