# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:51:39 2021

@author: NOTEBOOK
"""
import random

#The coin class simulates a coin that can be flipped

class Coin:
    #The __init__ method initialises the sideup data with the 'Heads'
    
    def __init__(self):
        self.sideup = 'Heads'
        
        #The toss method generates a random number in the range 0 to 1
        #If he number is 0, then sideup= Heads, else, sideup = tails
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup ='Heads'
        else:
            self.sideup ='Tails'
            
    #The get_sideup method returns the value refeerenced by sideup
    
    def get_sideup(self):
        return self.sideup
    
# The main function
def main():
    #Create an object from the coin class
    my_coin = Coin()
    
    #display the side of the coin that is facing up
    print('This side is up:', my_coin.get_sideup())
    
    #Toss the coin
    print('I am tossing the coin...')
    my_coin.toss()
    
    #display the side of the coin that is facing up
    print('This side is up:', my_coin.get_sideup())
    
#Call the main function
main()
    
                
        