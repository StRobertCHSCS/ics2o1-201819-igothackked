
'''
-------------------------------------------------------------------------------
Name:		windchill_factor.py
Purpose:	uses temperature in celsius and and wind speed and calculates the windchill factor

Author:	Cho.J

Created:	date in 24/02/2019
------------------------------------------------------------------------------
'''

#GET the temperature in celsius and wind speed

temp = int(input("What is the temperature in celsius? "))
wind = int(input("What is the wind speed (km/h)? "))

#COMPUTE wind chill factor = 13.12 + (.6215 x T) - (11.37 x V0.16) + (.3965 x T x V0.16)  where T is temperature and V is windspeed.

wind_chill = 13.12 + (0.6215*temp) - (11.37*wind**0.16) + (0.3965*temp*wind**0.16)

#output

print("If the temperature is ", temp, "and the wind speed is ", wind, "the wind chill will be ", round(wind_chill))