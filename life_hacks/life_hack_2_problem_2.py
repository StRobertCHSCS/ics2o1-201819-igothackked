
'''
-------------------------------------------------------------------------------
Name:		classifies_triangle.py
Purpose:	tells you what the name of the triangle is depending on the three angles in degrees

Author:	Cho.J

Created:	date in 25/03/2019
------------------------------------------------------------------------------
'''

#GET angle_one, angle_two, and angle_three
angle_one = int(input("Enter the first angle "))
angle_two = int(input("Enter the second angle "))
angle_three = int(input("Enter the third angle ")) 

#CHECK if the triangle is equilateral, isosceles, scalene or not a triangle
if angle_one == 60 and angle_two == 60 and angle_three == 60:
    print("The triangle is Equilateral")

elif angle_one + angle_two + angle_three == 180 and angle_one == angle_two or angle_two == angle_three or angle_three == angle_one:
    print("The triangle is Isosceles")

elif angle_one + angle_two + angle_three == 180:
    print("The triangle is Scalene")

else:
    print("ERROR")
