# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:23:26 2020

@author: NOTEBOOK
"""

#This program searchs the coffee.txt file
def main():
    #Create a flag variable
    found = False
    #get the searched item
    search = input('Type in the description of the coffee: ')
    #Open the coffee.text file
    coffee_file = open(r'C:\Python projects\python_exercises\files\coffee.txt','r')
    #Read the first line into memory
    descr = coffee_file.readline()
    while descr != '':
        qty = coffee_file.readline()
        descr = descr.rstrip('\n')
       #Check if the item does exist
        if descr == search:
           #Display the fields
           print ('Description:',descr)
           print('quantity:',qty )
          # Set the flag to true
           found = True
        #REad the ext description
        descr = coffee_file.readline()
    coffee_file.close()
    if not found:
        print('The item was not found in the file')
    coffee_file.close()
main()