# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:35:11 2019

@author: NOTEBOOK
"""

def main():
    print ('First Rectangle Details')
    length1 = float(input('Enter length: '))
    width1 = float(input('Enter width: '))
    area_1 = length1 * width1
    print('The area of the Rectangle is',format(area_1,'.2f'))

# Area 2
    print ('second Rectangle Details')
    length2 = float(input('Enter length: '))
    width2 = float(input('Enter width: '))
    area_2 = length2 * width2
    print('The area of the Rectangle is',format(area_2,'.2f'))

    if area_1 > area_2:
        print('The First rectangle has a larger area')
    elif area_1 < area_2:
        print('The second rectangle has a larger area') 
    else:
        print('The rectangles are of the same size')
    
main()
     
    