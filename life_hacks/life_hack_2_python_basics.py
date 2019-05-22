'''
-------------------------------------------------------------------------------
Name:		mr.fabroas_chicken.py
Purpose:	after you input the number of students and how many pieces
of chicken there is you will see how many pieces of chicken the students
and mr.fabroa will get

Author:	Cho.J

Created:	date in 28/02/2019
------------------------------------------------------------------------------
'''

#GET the number of studends in the class, get the number of chicken pieces
students= int(input("How many students are in Mr.Fabroa's class?: "))
chicken= int(input("How many pieces of chicken are there: "))

#COMPUTE number of chicken//number of students, number of chicken%number of students
chicken_for_students= chicken//students
chicken_for_mrFabroa= chicken%students

#DISPLAY how much chicken will mr.fabora and the children get
print("Each student will get", chicken_for_students, "pieces of chicken")
print("Mr.Fabroa will get", chicken_for_mrFabroa, "pieces of chicken")