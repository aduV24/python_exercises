# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:43:36 2020

@author: NOTEBOOK
"""

#This program uses a fuction to create a list
#The function returns a reference to the list

def main():
    #get the list
    numbers = get_values()
    print('The numbers in the list are:')
    print(numbers)



def get_values():
    #Create an empty list
    values = []
    #Create a variable to control the loop
    again = 'y'
    while again == 'y':
        num = float(input('Enter a number: '))
        values.append(num)
        print('Do you want to do this again?')
        again = input('y = yess, anything else = no: ')
        
    return values

main()