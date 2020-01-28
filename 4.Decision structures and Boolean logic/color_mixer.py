# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:13:30 2019

@author: NOTEBOOK
"""

def main():
    g = 'green'
    o = 'orange'
    p = 'purple'
    print('')
    print('Welcome to your Color mixing application '+
          'Please be aware that you can only input '+
          'primary colours(red,blue,yellow)')
    slot_1 = input('Enter color 1: ')
    slot_2 = input('Enter color 2: ')
    
    print('')
    
    if (slot_1 == 'red' and slot_2 == 'blue') \
      or (slot_1 == 'blue' and slot_2 == 'red'):
        print ('Colour mixture results in', p)
   
    elif  (slot_1 == 'red' and slot_2 == 'yellow')\
      or (slot_1 == 'yellow' and slot_2 == 'red'):
        print ('Colour mixture results in', o)
        
    elif (slot_1 == 'yellow' and slot_2 == 'blue') \
      or (slot_1 == 'blue' and slot_2 == 'yellow'):
        print ('Colour mixture results in', g)
   
    else:
        print('')
        print('Error!!!!     please input primary colors only!!')

        
main()
    