# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:22:58 2021

@author: NOTEBOOK
"""

class BankAccount():
    #The __init__ method accepts an arguement for the account's balance.
    #It is assigned to the__balance attribute.
    
    def __init__(self, bal):
        self.__balance = bal
        
    #The deposit ,method makes a deposit into the account
    
    def deposit(self, amount):
        self.__balance += amount
        
    # The withdraw method withdraws an amount from the account
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount 
        else:
            print('Error: insufficient funds')
            
    #The get_balance method returns the account balance
    def get_balance(self):
        return self.__balance
    
    #The __str__ method returns a stirng indicating the object's state
    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
    
        