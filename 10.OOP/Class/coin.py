# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:51:39 2021

@author: NOTEBOOK
"""
import random

#The coin class simulates a coin that can be flipped

class Coin:
    #The __init__ method initialises the __sideup data with the 'Heads'
    
    def __init__(self):
        self.__sideup = 'Heads'
        
        #The toss method generates a random number in the range 0 to 1
        #If he number is 0, then __sideup= Heads, else, __sideup = tails
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup ='Heads'
        else:
            self.__sideup ='Tails'
            
    #The get_sideup method returns the value referenced by __sideup
    
    def get_sideup(self):
        return self.__sideup
    





    
                
        