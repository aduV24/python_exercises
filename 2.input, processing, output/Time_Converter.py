# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:54:12 2019

@author: NOTEBOOK
"""

#Get the number of seconds from user

secs = float(input("Enter the number of seconds: "))

# Calculate the number of hours
hrs = secs//3600

# Calculate the number of minutes
mins = (secs % 3600) // 60

# Calutale the number of seconds
seconds = (secs % 3600) % 60 

# Give the results
print ("hours: ", hrs)
print ("minutes: ", mins)
print ("seconds: ", seconds)

print ('The total amount os hours spent is', hrs , sep='--------')
print ('Mon\nTues\tWed')
print ('Thur\tFri\tFri')