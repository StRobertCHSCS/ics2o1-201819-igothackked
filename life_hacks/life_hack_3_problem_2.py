'''
-------------------------------------------------------------------------------
Name:		average_km_driven_per_day.py
Purpose:	this program tells you how long it took for you to drive 100km, by taking your distance
            for each day and then giving the average of how much you drive each day.

Author:	Cho.J

Created:	date in 25/04/2019
------------------------------------------------------------------------------
'''

#MAKE your counters
total_distance = 0
total_drives = 0

#GET and COMPUTE how many times the loops runs and count
while total_distance<100 + 1:
    travelled = int(input("Enter the distance traveled for the day: "))
    total_distance = total_distance + travelled
    total_drives = total_drives + 1

#PRINT the total number of drives and the average km driven a day
print("It took", total_drives, "days to surpass the 100km driven")
print("The average distance driven per day is", total_distance/total_drives, "km")









