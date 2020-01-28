# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:11:09 2019

@author: NOTEBOOK
"""

def main():
    ask = 'y'
    while ask == 'y':
        purchase = int(input('ENter total number of packages purchased: '))
        global amount 
        amount = purchase * 99
        if purchase >=10 and purchase <=19:
           discount_20()
            
        elif purchase >=20 and purchase <=49:
            discount_30()
           
        elif  purchase >=50 and purchase <=99:
            discount_40()
            
        elif purchase >=100:
            discount_50()
            
        elif purchase >=0 and purchase <=9:
             print ('Total = $',format(amount,',.2f'),sep='')
             
        else:
             print ('Errorrrrr!!!!')
          
    ask = input("Do you wanna perform another operation?(Put y for yes and n for no): ")
            
         
        
def discount_20():
    discount = 0.02 * amount
    tot_pur = amount - discount
    print ('Discount = $',format(discount,',.2f'),sep='')
    print ('Total = $',format(tot_pur,',.2f'),sep='')
        
def discount_30():
    discount = 0.03 * amount
    tot_pur = amount - discount
    print ('Discount = $',format(discount,',.2f'),sep='')
    print ('Total = $',format(tot_pur,',.2f'),sep='')
        
    
def discount_40():
    discount = 0.04 * amount
    tot_pur = amount - discount
    print ('Discount = $',format(discount,',.2f'),sep='')
    print ('Total = $',format(tot_pur,',.2f'),sep='')
        
    
def discount_50():
    discount = 0.05 * amount
    tot_pur = amount - discount
    print ('Discount = $',format(discount,',.2f'),sep='')
    print ('Total = $',format(tot_pur,',.2f'),sep='')
    
    
    
    
        
    
main()
