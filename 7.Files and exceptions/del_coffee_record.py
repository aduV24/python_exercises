# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:04:04 2020

@author: NOTEBOOK
"""

#This program searchs the coffee.txt file
def main():
    import os
    #Create a flag variable
    found = False
    #get the searched item
    search = input('Type in the description of the coffee: ')
    #Open the coffee.text file
    temp_file = open(r'C:\Python projects\python_exercises\files\temp.txt','w')
    coffee_file = open(r'C:\Python projects\python_exercises\files\coffee.txt','r')
    #Read the first line into memory
    descr = coffee_file.readline()
    while descr != '':
        qty = coffee_file.readline()
        descr = descr.rstrip('\n')
        #Check if the item does exist
        if descr != search:
          temp_file.write(descr + '\n')
          temp_file.write(str(qty) + '\n')   
          # Set the flag to true
          found = True   
        #REad the ext description
        descr = coffee_file.readline()
    #Close both files
    coffee_file.close()
    temp_file.close()
   
    #Delete the coffee file
    os.remove(r'C:\Python projects\python_exercises\files\coffee.txt')
    #Rename the temp file to coffee.txt
    os.rename(r'C:\Python projects\python_exercises\files\temp.txt',r'C:\Python projects\python_exercises\files\coffee.txt')
    #If found or not found, display these messages
    if found:
        print('Item has been deleted')
    else:
        print('Item not found')
   
main()