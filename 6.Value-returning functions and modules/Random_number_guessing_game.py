# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 00:16:59 2020

@author: NOTEBOOK
"""
import random
def main():
    #Initialize counter 
    count = 0
    total = 0
    print('This is a program that generates a random number')
    #Ask user to start
    start = int(input('Please Enter 1 to start'))
    # Validation
    while start != 1:
        print ('Error!!!!!!, Enter 1 to start')
        start = int(input('Please Enter 1 to start'))
    #Loading..................
    print('Generating a number.........')
    print('number Generated, please take a guess between 1 - 100')
    #Generate number 
    num = random.randint(1,100)
    print (num)
    guess = int(input('Guess? '))
    while guess != num :
        count = 1
        total += count
        print('Wrong, try again ')
        guess = int(input('Guess? '))
    print()   
    print ('Yay!!!! you got it')
    print()
    print ('The total number of tries before the corect answer is',total)
    
    
main()