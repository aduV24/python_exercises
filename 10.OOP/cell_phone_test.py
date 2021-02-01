# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:47:32 2021

@author: NOTEBOOK
"""

# This program tests the cellphone class
from Class import cellphone

def main():
    #Get the phone data 
    man = input('Enter the manufacturer: ')
    mod = input('Enter model number: ')
    retail = float(input('Enter the retail price: '))
    
    #Create an instance of the cellphone class
    phone = cellphone.Cellphone(man, mod,retail)
    
    #Display the data that was entered 
    print('Here is the data you entered.')
    print('-----------------------------')
    print('Manufacturer',phone.get_manufact())
    print('Model number:', phone.get_model())
    print('Retail price: $',format(phone.get_retail_price(),',.2f'),sep='')
    
#Call the main function
main()
    
    