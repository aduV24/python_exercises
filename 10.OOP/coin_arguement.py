# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:54:21 2021

@author: NOTEBOOK
"""

# This program passes a coin object as an arguement to a function
from Class import coin

#main function 
def main():
    #Create a coin object
    my_coin = coin.Coin()
 
    #This will display heads
    print(my_coin.get_sideup())
    
    #Pass the object to the flip coin function
    flip(my_coin)
    
    #this might display Heads or it might display tails 
    print(my_coin.get_sideup())
    
#This flip function flips a coin
def flip(coin_obj):
    coin_obj.toss()
    
    
    
#Call main function    
main()
