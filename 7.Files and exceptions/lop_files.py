# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:11:06 2020

@author: NOTEBOOK
"""

def main():
    # Get the number of sales days
    sales_days = int(input('Please Enter the number of sales days:'))
    # create/open sales.txt file
    sales_file = open(r'C:\Python projects\files\sales.txt','w')
    #Get the number of sales for each day and write it to files
    for num in range(1, sales_days+1):
        #Get the number of sales
        sales = int(input('Enter sales for day' + str(num) + ': '))
        #Write the number of sales into files 
        sales_file.write(str(sales) + '\n')
        
     #Close the file   
    sales_file.close()   
    print('Data has been written to sales.txt')
    
    
    
    
main()