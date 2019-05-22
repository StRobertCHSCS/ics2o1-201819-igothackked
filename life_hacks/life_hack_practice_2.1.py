

'''
-------------------------------------------------------------------------------
Name:		right_angle_triangle?.py
Purpose:	gets three lenghts of a triangle and calculates if it is a right angle triangle or not/

Author:	Cho.J

Created:	date in 19/03/2019
------------------------------------------------------------------------------
'''

#GET the lengths of the 3 lengths
one = int(input("Enter first number: "))
two = int(input("Enter second number: "))
three = int(input("Enter third number: "))

#CHECK if it is a right angle triangle
if one**2 + two**2 == three**2 or two**2 +three**2 == one**2 or three**2 + one**2 == two**2:
    print("This is a right angle triangle. ")

else:
    print("This is not a right angle triangle. ")