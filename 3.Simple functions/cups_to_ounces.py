# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:40:11 2019

@author: NOTEBOOK
"""
#This program converts cups to ounces

def main():
    #Display the intro screen
    intro()
    #Get the number of cups
    cups = int(input("Enter number of cups: "))
    #Convert the cups to ounces
    cups_to_ounces(cups)
    
    
#Intro function displays an introductory screen 
def intro():
    print("This program converts cups to ounces")   
#cups_to_ounces accepts the nuber of cups  
#and dispay the equivalent number of ounces
def cups_to_ounces(no_of_cups):
    ounces = no_of_cups * 8
    print("Amount in ounces = ", format(ounces,'.2f'))

 #Call the main function   
main()
    