# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:03:13 2019

@author: NOTEBOOK
"""

# This program sums up 5 numbers entered by th user
def main():
    print('Please Enter numbers you wish to add')
    total = 0.0
    for number in range(5):
        number = int(input ('Enter number: '))
        total += number 
    print ('')    
    print ('Total = ', total)
    
main()