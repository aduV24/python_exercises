# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:36:48 2020

@author: NOTEBOOK
"""

#This program Gets emloyees data from the user and saves them in
#file employess.txt

def main():
    #Header
    print('Olustar Nig. Ltd. Employees Data collection')
    #Get the number of emloyees
    emp_count = int(input('Enter the number of Employees: '))
    #Open a file
    emp_file = open(r'C:\Python projects\python_exercises\files\employees.txt','w')
    #Get each Employee's data and write into file
    for count in range(emp_count):
        #Get the data from an employee
        print('Enter the data for employee #',count + 1,sep = '')
        name = input('Name: ')
        id_num = input('ID number: ')
       #write the data into file
        dept = input('Department: ')
        emp_file.write(name+'\n')
        emp_file.write(id_num+'\n')    
        emp_file.write(dept+'\n')
        print()
     #Close the file   
    emp_file.close() 
     #Confirmation message
    print('Data has been written to employees.txt')
    
    
main()    