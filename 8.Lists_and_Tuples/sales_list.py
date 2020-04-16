# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:49:07 2020

@author: NOTEBOOK
"""
#the num_days holds the constant for the number of days
#that we wil gather data for 
num_days = 5
def main():
    #Create a list 
    sales = [0] * num_days
    print('Enter the sales for each day')
    #Create a variable to hold an index
    index = 0
    #Get the sales for each day
    while index < len(sales):
        amt = int(input('Day#'+str(index+1)+': '))
        sales[index] = amt
        index += 1
    print()
    print('Here are the values you entered')
    print('--------------------------------')
    #Display the sa;es gotten
    for value in sales:
        print(value) 
       
main()
