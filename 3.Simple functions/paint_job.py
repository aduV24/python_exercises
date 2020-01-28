# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:32:17 2019

@author: NOTEBOOK
"""

def main():
    sq_feet = float(input('Enter number of sq feet: '))
    gallon_price = float(input('Price per gallon: '))
    show_gallons(sq_feet)
    show_hours(sq_feet)
    show_paintcost(gallon_price, sq_feet)
    show_labour(sq_feet)
    show_total()
    
def show_gallons(sq_feet):
    gallon = sq_feet / 115
    print ('')
    print ('Number of Gallon = ',format(gallon, ',.2f'))
    
def show_hours(sq_feet):
    hours = sq_feet / 14.375
    print ('Number of Hours = ', format(hours, ',.2f'))
    
def show_paintcost(price,sq_feet):
    global paint_cost
    paint_cost = price * ( sq_feet / 115)
    print ('Cost of paint = $', format(paint_cost, ',.2f'), sep='')
    
def show_labour(sq_feet):
    global labour
    labour = 20 * (sq_feet / 14.375)
    print ('Cost of labour = $', format(labour, ',.2f'), sep='')
    
def show_total():
    total = paint_cost + labour
    print ('total Cost  = $', format(total, ',.2f'), sep='')
    
    
main()
    
    
    
    