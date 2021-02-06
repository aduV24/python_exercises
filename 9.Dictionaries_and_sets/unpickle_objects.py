# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:05:31 2021

@author: NOTEBOOK
"""

#This program demonstrates unpickling
import pickle
#main functon
def main():
    end_of_file = False #To demonstrate end of file
    #open a file for binary reading
    input_file = open('info.dat','rb')
    
    #read to the r=end of that file
    while not end_of_file:
        try:
            #unpickle the next object
            person =pickle.load(input_file)
            #Display the object
            display_data(person)
            
        except EOFError:
            #Set flag to indicate the end of file has been reached
            end_of_file = True 
    
    #Close the file
    input_file.close()
    
# The display_data function displays the perso data 
#in the dictionary that is passed as an arguement

def display_data(person):
    print('Name:',person['Name'])
    print('Age:',person['Age'])
    print('Weight:',person['Weight'])
    print()
    
#Call the main function
main()
            