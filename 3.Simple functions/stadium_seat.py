# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:15:35 2019

@author: NOTEBOOK
"""

def main():
    a = int(input('Enter umber of classA tickets: '))
    b = int(input('Enter umber of classB tickets: '))
    c = int(input('Enter umber of classC tickets: '))
    show_income(a,b,c)
    
    
def show_income(a,b,c):
    income = (a * 15) +(b * 12) + (c * 9)
    print ('Total income = $',format(income,',.2f'), sep='')
    
    
main()
    