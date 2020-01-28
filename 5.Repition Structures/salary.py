# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:38:37 2019

@author: NOTEBOOK
"""
#This program displays the total earnings of a worker over a number of days in dollars
# starting from 1 penny and doubling each day
def main():
    #Get number of days
    days = int(input('Enter number of days: ' ))
    #Print Headers
    print('Days\tEarnings')
    print('---------------------')
    #Initialize first earning
    starter = 1.0
    #initialize acummulator
    total = 0.0
    for num in range(days):
        #Calculate and display earnings
        earnings = starter * (2 ** (num))
        print('Day',num + 1,'\t', earnings)
        total += earnings 
    dollar_earnings = total / 100
    print('---------------------') 
    print('total earnings in dollars is $',format(dollar_earnings,',.2f'), sep ='')
main()