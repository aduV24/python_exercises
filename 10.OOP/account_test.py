# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:30:22 2021

@author: NOTEBOOK
"""

#This program demonstrates the bankaccount class
from Class import bankaccount

def main():
    #Get the starting price
    start_bal = float(input('Enter your starting balance: '))
    
    #Create a bankacoount object
    savings = bankaccount.BankAccount(start_bal)
    
    #Deposit the users paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account ')
    savings.deposit(pay)

    #Display the balance
    print(savings)
    
    #Get the amount to withdraw 
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account')
    savings.withdraw(cash)
    
     #Display the balance
    print(savings)

#Call the main function 
main()        
    