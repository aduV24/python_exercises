# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:40:47 2020

@author: NOTEBOOK
"""
total =0.0


input_file  = open(r'C:\Python projects\files\sales.txt','r')
for line in input_file:
    amount = float(line)
    print(format(amount,'.2f'))
    total += amount
    
print(format(total,'.2f'))