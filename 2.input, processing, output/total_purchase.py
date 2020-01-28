# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:02:17 2019

@author: NOTEBOOK
"""

print("Please enter the amount of each item")

item1=(float(input('Item 1: ')))
item2=(float(input('Item 2: ')))
item3=(float(input('Item 3: ')))
item4=(float(input('Item 4: ')))
item5=(float(input('Item 5: ')))

sub_total = item1 + item2 + item3 + item4 + item5
tax = sub_total * 0.06
total = sub_total + tax

print ("Subtotal: ", format(sub_total, '10,.2f'))
print ("Sales tax: ", format(tax, '9,.2f'))
print ("Total: ", format(total, '13,.2f'))