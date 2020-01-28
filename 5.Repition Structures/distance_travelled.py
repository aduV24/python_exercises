# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 23:18:03 2019

@author: NOTEBOOK
"""

def main():
    speed = int(input('What is the speed of the vehicle in mph? '))
    hours = int(input('How many hours has it traveled? '))
    print('Hour\t\tDistance traveled(Miles)')
    print('-------------------------------------')
    for num in range(hours):
        distance = speed *(num + 1)
        print (num + 1,'\t\t\t',distance)
    
main()