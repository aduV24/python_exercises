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
    while count == 0:
        try:
            #Ask user to start
            start = int(input('Please Enter 1 to start: '))
            # Validation
            while start != 1:
                print ('Error!!!!!!, Enter 1 to start')
                start = int(input('Please Enter 1 to start'))
            #Loading..................
            print('Generating a number.........')
            print('number Generated, please take a guess between 1 - 10')
            #Generate number 
            num = random.randint(1,10)
            #print (num)
            guess = int(input('Guess? '))
            count = 1
            while guess != num :
                total += count
                #Check if t
                if guess > num:
                    print('Wrong,too high')
                else:
                    print('Wrong,too low')
                guess = int(input('Guess? '))
            print()   
            print ('Yay!!!! you got it')
            print()
            print ('The total number of tries before the correct answer is',total+1) 
        except ValueError:
            print('Enter numberic integers')
            total = 0

    
    
main()