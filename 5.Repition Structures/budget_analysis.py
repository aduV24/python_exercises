# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 21:55:09 2019

@author: NOTEBOOK
"""

# This program perfroms monthly Budget Ananlysis
def main():
    global budget
    #Ask for budget and total number of expenses
    budget = float(input('Enter your budget (in dollars): '))
    num_expenses = int(input('Enter number of expenses: '))
   
    # initialize accumulator
    global total
    total = 0.0
   
    #Headers
    print('Expenses')
    print('-------------')
    
    #Accept expenses and print total
    for num in range(num_expenses):
        expenses = float(input(str(num + 1)+') '))
        total += expenses
    print('Total Expenses = $',format(total,',.2f'), sep='')
   
    #Call the display_comment function
    display_comment()
    
    
#The display_comment function run checks if its over or under budget
def display_comment():
    print('---------------------------------------')
    if budget >= total:
        rem = float(budget - total)
        print('You are good to go, your budget covers your expenses') 
        print('You are under budget by $',format(rem,',.2f'),sep='')
    else:
        rem = float(total - budget)
        print('You are way over budget!!!!!')
        print('You are over budget by $',format(rem,',.2f'),sep='')
    
    
main()