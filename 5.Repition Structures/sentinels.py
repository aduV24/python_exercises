# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:44:14 2019

@author: NOTEBOOK
"""

# This program is used to calculate tax for purchased properties
TAX_FACTOR = 0.065
def main():
    print ('Enter the lot size or enter 0 to quit program')
    # Create a variable to control the loop
    lot = int(input('Enter lot size: '))
    #continue to process as long as the lot is not 0
    while lot != 0:
        price = int(input('Enter property price:'))
        #Calculate and print the tax
        tax = price * TAX_FACTOR
        print ('Tax = ', tax)
        #Get the next lot
        lot = int(input('Enter lot size: '))
    print('Exiting program.......')
    
    
main()