# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 01:02:07 2020

@author: NOTEBOOK
"""
import random
def main():
    global user_choice
    global com
   # Introduction
    print('Welcome to ROck paper Scissors Game!!!')
    # COmputer makes choice
    com = com_choice(random.randint(1,3))
    #print (com)
   #Get user's choice
    try:
       user_choice = str(input('Enter rock, paper or scissors: '))
       
        #Error handler
       while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
            print('')
            print('Error pls try again','Enter on rock, paper or scissors')
            user_choice = str(input('Enter rock, paper or scissors: '))
       print('Computer:',com)
      
        #Deadlock handler
       while user_choice == com:
            print('')
            print('Its a tie please play again')
            user_choice = str(input('Enter rock, paper or scissors: '))
            com = com_choice(random.randint(1,3))
    except ValueError:
        print('Enter string (rock, paper or scissors)')
   
   
    print('')
    print(result(user_choice))
    
    
    
    
    
def com_choice(choice):
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    elif choice == 3:
        return 'scissors'
    
def result(user_choice):
    if (user_choice == 'rock' and com == 'scissors'):
        return 'The user wins' 
    elif (user_choice == 'scissors' and com == 'rock'):
        return 'The computer wins'
 
    if  (user_choice == 'rock' and com == 'paper'):
        return 'The computer wins' 
    elif (user_choice == 'paper' and com == 'rock'):
        return 'The user wins' 
   
    if (user_choice == 'scissors' and com == 'paper'): 
        return 'The user wins'
    elif (user_choice == 'paper' and com == 'scissors'):
      return 'The computer wins'

    
        
        
    
    
   
    
main()