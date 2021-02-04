# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:17:34 2021

@author: NOTEBOOK
"""
from Class import coin
#This function imports the coin module and 
#creates an instance of the coin class
def main():
    #Create an object from the coin class
    my_coin = coin.Coin()
    
    #display the side of the coin that is facing up
    print('This side is up:', my_coin.get_sideup())
    
    #Toss the coin
    print('I am tossing the coin...')
    my_coin.toss()
    
    #display the side of the coin that is facing up
    print('This side is up:', my_coin.get_sideup())
    
    #Call the main function
    
    
main()