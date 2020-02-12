# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:30:42 2020

@author: NOTEBOOK
"""

#This program shows the records in the cofee.txt file
def main():
    #open the coffee.txt file
    coffee_file = open(r'C:\Python projects\python_exercises\files\coffee.txt','r')
    #Header
    print('These are the items you have in record')
    print('----------------------------------------')
    #Read the first description field into memory
    descr = coffee_file.readline()
    #If a description is read continue processing
    while descr != '':
        #Read the next field into memory
        qty = coffee_file.readline()
        #Strip the fields
        descr = descr.rstrip('\n')
        qty = qty.rstrip('\n')
        #Display the fields
        print ('Description:',descr)
        print('quantity:',qty )
        #Read the next field into memory
        descr = coffee_file.readline()
        
    #Close coffee.txt file
    coffee_file.close()
    
        

        
main()