'''
-------------------------------------------------------------------------------
Name:		hours_to_days.py
Purpose:	converts hours into days

Author:	Cho.J

Created:	date in 22/02/2019
------------------------------------------------------------------------------
'''

#GET number of hours
day= int(input("What is the number of hours: "))

#COMPUTE days= how many days hours= how many hours left
days= (day//24)
hours= (day%24)

#PRINT how many days and hours
print (day, "= ", days, "days and", hours, "hours" )