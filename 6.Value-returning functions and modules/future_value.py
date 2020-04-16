# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 00:02:53 2020

@author: NOTEBOOK
"""

def main():
    try:
        # Get the necesarry inputs
        p_value = int(input("Enter the acccount's present value: "))
        m_rate = float(input("Enter the monthly interest rate(%): "))
        time = int(input("Enter Time(Months): " ))
        
        #display future value
        future_value = cal_future(p_value,m_rate,time)
        print('The future is ',format(future_value,',.2f'))
    except ValueError:
        print('PLease Enter integers for present values and time')
    
#The cal_future function calcuates and gives the future value
def cal_future(p,m,t):
    f = p * ((1+ m) ** t)
    return f
    
    
main()