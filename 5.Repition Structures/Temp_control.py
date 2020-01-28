# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:41:13 2019

@author: NOTEBOOK
"""

MAX_TEMP = 102.5

def main(): 
    temperture = float(input("Please Enter temperature: "))
    while temperture < 0:
        print('Temperature cannot be less than 0')
        temperture = float(input("Please Enter temperature: "))
    while temperture > 102.5:
        print("Turn down the thermostat, wait for 5 mins")
        print("")
        temperture = float(input("Please Enter temperature: "))
    
    print("Temperature is acceptable, Check back after 15mins")
        
    
main()