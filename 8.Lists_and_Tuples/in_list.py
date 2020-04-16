# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:32:47 2020

@author: NOTEBOOK
"""

#This program demostrates how to use the in operator
#used with listAV13
def main():
    #Create teh list
    eng_num = ['AV143','SO127','RW224','DC465','DN111']
    #Get a product number to search for
    search =input('Enter a product number: ')
    if search in eng_num:
        print(search,'Was found in the list')
    else:
        print(search,'was not found')
        
main()