# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:38:48 2020

@author: NOTEBOOK
"""

#This program adds invetory to the coffee.txt file
def main():
    #Header
    print('Enter the following data')
    #Create a variable to control the loop 
    another = 'y'
    # open the coffee filein append mode
    coffee_file = open(r'C:\Python projects\python_exercises\files\coffee.txt','a')
   
    while another == 'y' or another == 'Y':
    #Get data
        descr = input('Description: ')
        qty = float(input('Quantity(lbs): '))
     #Write data into record
        coffee_file.write(descr+'\n')
        coffee_file.write(str(qty) + '\n')
        another = input('Add nother coffee?(y = yes n= no): ')
    #Close file
    coffee_file.close()
   
    #Display confirmation
    print('Data has been appended to coffee.txt')    
        
    
main()