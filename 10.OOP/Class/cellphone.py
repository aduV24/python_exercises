# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:32:40 2021

@author: NOTEBOOK
"""
# The cellphone class holds data about a cellphone

class Cellphone:
    # The __init__ initializes the attributes 
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price
        
    #The set_manufat method accepts an argument for the phone's manufacturer
    def set_manufact(self, manufact):
        self.__manufact = manufact
        
    #The set_model method accepts an argument for the phone's model
    def set_model(self, model):
        self.__model = model
        
    #The set_retail_price method accepts an argument for the phone's model
    def set_retail_price(self, price):
        self.__retail_price = price
        
    #The get_manufact method returns the phone's manufacturer
    def get_manufact(self):
        return self.__manufact
    
     #The get_model method returns the phone's manufacturer
    def get_model(self):
        return self.__model
    
     #The get__retail_price method returns the phone's manufacturer
    def get_retail_price(self):
        return self.__retail_price
    
    
    
   
    
        
    
        
        
         

            
        