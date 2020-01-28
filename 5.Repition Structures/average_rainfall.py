# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 23:28:42 2019

@author: NOTEBOOK
"""
#This progarm calculates the amount of rainfall in a certain period of time(Years)
def main():
    #initialize accumulator
    total = 0.0
    #Get number of years
    num_years = int(input ('Enter number of years: '))
    for years in range (num_years):
        print ('Year',(years + 1),)
        print('Amount of rainfall(inches)')
        print ('----------------------------')
        
        for num_months in range (12):
            #get amount of rainfall per month
            amt_rainfall =float(input('Month' + str(num_months + 1) +':- '))
            total += amt_rainfall
            print ()
    average = total / (num_years * 12)
    #Dispaly total and average rainfall
    print ('----------------------------')
    print('Total number of months =',(num_years * 12))
    print('Total amount of rainfall(inches):-',total)
    print('Average Rainfall per month is:-',average)
main()
