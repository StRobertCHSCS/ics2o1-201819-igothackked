

'''
-------------------------------------------------------------------------------
Name:		minutes_to_days.py
Purpose:	converts minutes into days, hours, minutes

Author:	Cho.J

Created:	date in 22/02/2019
------------------------------------------------------------------------------
'''

#PRINT
minute= int(input("How many minutes: "))

#COMPUTE
days= minute//1440
hours_left= minute%1440
hours= hours_left//60
days_left= minute%60

#PRINT
print(minute, "minutes=", days, "days, ", hours, "hours, ", days_left, "minutes")

