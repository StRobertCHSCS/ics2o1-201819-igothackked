'''
-------------------------------------------------------------------------------
Name:		resetting_your_password.py
Purpose:	to make a new password that does not contain the old password in it

Author:	Cho.J

Created:	date in 25/04/2019
------------------------------------------------------------------------------
'''

# GET the new and old password
old = input("Enter the current password: ")
new = input("Enter the new password: ")
found = False
# COMPUTE the variables
num_old = len(old)
num_new = len(new)

# COMPUTE to see if it is right or wrong
for i in range(num_old):
    if old == new[i:num_old + 1]:
         found = True

for i in range(num_old):
    if old == new[i:num_old]:
        found = True

# PRINT to see if it is right or wrong
if found == True:
    print("This password is not reset. the new password can not contain the old password")

else:
    print("Password has been reset")