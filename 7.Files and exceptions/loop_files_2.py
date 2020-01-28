# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:24:07 2020

@author: NOTEBOOK
"""
def main():
    ''' sales_file = open(r'C:\Python projects\files\sales.txt','r')
   line = sales_file.readline()
   while line != '':
       amount = float(line)
       print (format(amount, '.2f'))
       line = sales_file.readline()
       
   sales_file.close()      ''' 
  
    sales_file = open(r'C:\Python projects\files\sales.txt','r')
    for rrr in sales_file:
       amount = float(rrr)
       print (format(amount, '.2f'))
      
       
    sales_file.close()       
   
   
    
    
main()    
