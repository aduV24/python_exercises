# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:44:18 2020

@author: NOTEBOOK
"""
import random
#This program fills lists with random numbers

def main():
    rows = 5
    columns =4
   #Create a two-dimensional list
    list=[[0]*4,
          [0]*4,
          [0]*4,
          [0]*4,
          [0]*4
         ]
   #Fill the list with random num
    for r in range(rows):
        for c in range(columns):
            list[r][c] = random.randint(1,100)
   #Print list
    print(list)
    
        
main()