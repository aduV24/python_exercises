# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:08:04 2020

@author: NOTEBOOK
"""
num_emp = 6
#This program calculates grosspay for employees of a bar

def main():
    print('WELCOME')
    #Create Empty list
    emp_pay = []
    
    #Add Hours to list
    for i in range(6):
        hrs = float(input('Enter Hours worked by Employee#'\
                          +str(i+1)+': '))
        emp_pay.append(hrs)
  
    #Get employee rate
    rate = float(input('Enter the rate in USD: '))
    print()
  
    #Calclate and display Gross pay
    print('Gross pay for Employess')
    print('--------------------------')
  
    #initalize accumulator
    total = 0.0
    for i in range(6):
        gross_pay = emp_pay[i] * rate
        print('Gross pay for Employee#',i+1,': $',\
              format(gross_pay,'.2f'),sep='')
        total += gross_pay
    print('-------------------------------------')    
    print('Total: $',format(total,',.2f'),sep='')

main()