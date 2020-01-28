# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:43:18 2020

@author: NOTEBOOK
"""

import random

def main ():
    #INITIALIZE ACUMMULATORS
    total_evens = 0
    total_odds = 0
    #Print Headers
    print('Number','\t','Status')
    print('-------------------------')
    for num in range (100):
        rand = random.randint(1,500)
        if is_even(rand):
            evens = 1
            total_evens += evens
            print(rand,'\t','Even')
        else:
            odds = 1
            total_odds += odds
            print(rand,'\t','Odd')
        
    print('')    
    print('Number of even numbers is', total_evens)
    print('Number of odd numbers is', total_odds)
    
        
        
 #The is_even function determines whether the number is even or odd       
def is_even(rand):
    if rand % 2 == 0:
       status = True
    else:
       status = False
        
    return status
        
main()