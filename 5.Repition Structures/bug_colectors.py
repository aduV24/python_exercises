# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 21:38:53 2019

@author: NOTEBOOK
"""

#This program accepts the number of bugs 
#collected over 7 days and displays the total
def main():
    #Intro / Headers
    print ('Bug collection calculator ') 
    print ('------------------------------')
    #initializing accumulator
    total = 0.0
    #Iterating collection of bugs 7 times 
    for num in range (7):
        bugs = int(input('Day'+ str(num+1) + ': '))
        #Keep running total
        total += bugs
        #Display Total bugs
    print ('Total number of bugs colected is',int(total))
                    
    
main()