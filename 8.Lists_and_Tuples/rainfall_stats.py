# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:23:36 2020

@author: NOTEBOOK
"""
#The program calculates and displays the total rainfall for the year, 
#the average monthly rainfall, and the months with 
#the highest and lowest amounts.

def main():
    #Create a list
    rain_fall = []
    #Get the amount of rainfall for each month
    print('Enter the amount of rainfall for each month')
    total = 0.0  
    for i in range(12):
        rainfall = float(input('Month #'+str(i+1)+': '))
        rain_fall.append(rainfall)
        total += rainfall 
    print()   
    #Calculate average
    avg = total / 12
    
    print('Total rainfal for the year is',format(total,'.2f'))
    
    print('The monthly average is',format(avg,'.2f') )
    
    index_max =  rain_fall.index(max(rain_fall))
    print('The maximum rainfall in a month is ',max(rain_fall),' on month#',\
         index_max+1,sep='')
    
    index_min =  rain_fall.index(min(rain_fall))
    print('The minimum rainfall in a month is ',min(rain_fall), ' on month#',\
         index_min+1,sep='')
main()

