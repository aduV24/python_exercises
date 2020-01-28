# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:35:37 2019

@author: NOTEBOOK
"""

def main():
    total = 0.0
    number = 5
    print('Enter a series of +ve number, enter a -ve number to end the series')
    while number >= 0:
        number = float(input('number: '))
        if number >= 0:
            total += number
        
    print('Total is',total)
        
main()