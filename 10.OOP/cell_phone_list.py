# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:02:07 2021

@author: NOTEBOOK
"""

#This program creates five cellphone objects and stores them in a list

from Class import cellphone

def main():
    #Get a list of cellphone objects
    phones = make_list()
    #Display the data in the list
    print("Here is the data you entered: ")
    display_list(phones)
    
    #The make_list() function gets data from the user for five phones 
    #The function returns a list of Cellphone objects containing the data
    
def make_list():
    #Create an empty list 
    phone_list =[]
    #Add five cellphone objects to the list 
    print('Enter data for five phones: ')
    for count in range(1,4):
    #Get the phone data
        print('Phone number '+ str(count) + ':')
        man = input('Enter the manufacturer: ')
        mod = input('Enter model number: ')
        retail = float(input('Enter the retail price: '))
        print()
        
        #Create a new Cellphone object in memory and assign it to the 
        #Phone variable
        phone = cellphone.Cellphone(man,mod,retail)
        
        #Add object to list 
        phone_list.append(phone)
        
  
    #return the list 
    return phone_list
    
#The display_list finction accepts a list containing cellphone obects as
#an arguement and displays the data stored in each data

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

#Call the main function

main()        
                
    
        
 