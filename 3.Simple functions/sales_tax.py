# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:12:01 2019

@author: NOTEBOOK
"""
def main():
    purchase = float(input("Enter the total amount of purchase: "))
    tax(purchase)
    
    
def tax(pur):
    sales_tax = pur * 0.04
    county_tax = pur * 0.02
    total_tax = sales_tax + county_tax
    total = pur + total_tax    
    print("Purchase = ",format(pur,',.2f'))
    print("state tax = ",format(sales_tax,',.2f'))
    print("County tax = ",format(county_tax,',.2f'))
    print("Total tax = ",format(total_tax,',.2f'))
    print("Grand Total = ", format(total, ',.2f'))
    
    
main()

    
    
