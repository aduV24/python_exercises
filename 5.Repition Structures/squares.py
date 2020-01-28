# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:26:36 2019

@author: NOTEBOOK
"""

# This program displays numbers and thir squares

def main():
    #INTRO
    print('This program lists numbers and their squares')
    #Create a variable to control the loop
    keep_going = 'y'
    while keep_going == 'y':      
        #Get the starting point
        start = int(input('Start:'))
        #Get the end limit
        end = int(input('Stop: '))
        # Print Table Headings 
        print("Number\tSquare")
        print("-------------------")
        #Print numbers and their squares
        for number in range(start, end +1):
            square = number ** 2
            print(number, '\t',square )
            #See if the user wnna do another one
        keep_going = input('Do you wanna perform another operation?' +
                           '(y for yes n for no): ')
        
        
main()
        