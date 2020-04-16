# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:01:35 2020

@author: NOTEBOOK
"""
#Demonstrates how to use the append method
def main():
   #Create and empty list
    name_list = []
    #Create a variablre that controls the loop
    again = 'y'
    while again == 'y':
        name = input('Enter a name: ')
        name_list.append(name)
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no: ')
        print()
        #Display the names in the list
        print('Here are the names you have entered')
        for name in name_list:
            print(name) 
main()
