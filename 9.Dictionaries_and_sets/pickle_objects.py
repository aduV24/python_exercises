# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:45:49 2021

@author: NOTEBOOK
"""

#This program demonstrates object pickling
import pickle
# main function

def main():
    again ='y'  #To control the loop repitition
    #Open a file for binary writing
    output_file = open('info.dat', 'wb')
   
    while again.lower() == 'y':
        #Get data about a person and save it
        save_data(output_file)
        #Does the user want more data?
        again = input('Enter more data? (y/n): ')
        
    #close the file
    output_file.close()
    
    #The save_data function gets a data about a person,
    #stores it in a dictionary
    #and then pickles the dictionary to the specified file

def save_data(file):
    #Create a empty dictionary
    person ={}
    #Get the data for one person and store in a ditionary
    person['Name'] = input('Name: ')
    person['Age'] = int(input('Age: '))
    person['Weight'] = float(input('Weight: '))
    
    #pickle the dictionary
    pickle.dump(person,file)
    
#Call the main function
main()
    
