# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:31:47 2020

@author: NOTEBOOK
"""
#This is a guess number game
import random
def main():
    print('Hello, What is your name?')
    name = input()
    secretnumber = random.randint(1, 10) 
    print("Well", name, "I am thinking of a number between and including 1-10")
    #Ask the player for a random number 
    for num in range(1,7):
        print('Take a guess.')
        guess = int(input())
        if guess > secretnumber:
            print('too high')
        elif guess < secretnumber:
            print('to low')
        else:
            break #Condition if the number is correct
    if guess == secretnumber:
        print('Good job',name,'you got it in', num, 'try(ies)')
    else:
        print("Oops!, you've exceeded your number of tries")
        print("Answer is",secretnumber)            
    
main()