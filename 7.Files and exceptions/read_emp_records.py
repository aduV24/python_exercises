# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:58:42 2020

@author: NOTEBOOK
"""

#This program reads records of employees and dislpay to the user

def main():
    #Header
    print('Olustar Nig. Ltd. Employees Records')
    emp_file = open(r'C:\Python projects\python_exercises\files\employees.txt','r')
    #Read the name field of record 
    name = emp_file.readline()
    #If there are more data to read continue processing
    while name != '':
         #Read Other fields
         id_num = emp_file.readline()
         dept = emp_file.readline()
         #Strip the '\n' for the data
         name = name.rstrip('\n')
         id_num = id_num.rstrip('\n')
         dept = dept.rstrip('\n')
         #Display the data
         print('------------------------')
         print ('Name:',name)
         print('ID NUmber:',id_num)
         print('Department:',dept)
         #Read the next name field in the record
         name = emp_file.readline()
    #Close the file
    emp_file.close()
             
         
main()

