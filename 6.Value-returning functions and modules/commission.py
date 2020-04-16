# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:14:06 2020

@author: NOTEBOOK
"""

#This program calculats  a salesperson's pay 

def main():
    try:
        #Get salesperson's monthly sales
        sales = get_sales()
        #Get amount of advanced pay
        advance = advanced_pay()
        #Determine comission rate
        comm_rate = det_comm_rate(sales)
        #Determine salesperson's pay
        pay = sales * comm_rate - advance
        print('The monthly pay is $',format(pay,'.2f'),sep='')
        # check for reinbursement
        if pay < 0:
            print('You have not sold enough you need to reimburse the company')

    except ValueError:
        print('Invalid Input, please enter numeric values')
        
def get_sales():   
        monthly_sales = float(input('Enter total monthly sales: ')) 
        return monthly_sales

def advanced_pay():
    print('Enter 0 if there is no advance pay')
    adv = float(input('Enter the advance payment: '))
    return adv

def det_comm_rate(sales):
    if sales < 10000 :
        rate = 0.1
    elif sales >= 10000 or sales < 15000:
        rate = 0.12
    elif sales >= 15000 or sales < 18000:
        rate = 0.14
    elif sales >= 18000 or sales < 22000:
        rate = 0.16
    else:
        rate = 0.18
    return rate
            
main()


    
    
