# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:02:09 2019

@author: NOTEBOOK
"""
def main():
    weight = float(input("Enter weight of package: "))
    if weight > 0 and weight <= 2:
        rate_per_kg = 1.10
        ship_fee = rate_per_kg * weight
        print("Rate per kg = $",format(rate_per_kg,',.2f'),sep='') 
        print ("The shipping fee is $",format(ship_fee,',.2f'),sep='')
    
    elif weight > 2 and weight <= 6:
        rate_per_kg = 2.20
        ship_fee = rate_per_kg * weight
        print("Rate per kg = $",format(rate_per_kg,',.2f'),sep='')
        print ("The shipping fee is $",format(ship_fee,',.2f'),sep='')
        
    elif weight > 6 and weight <= 10:
         rate_per_kg = 3.70
         ship_fee = rate_per_kg * weight
         print("Rate per kg = $",format(rate_per_kg,',.2f'),sep='')
         print ("The shipping fee is $",format(ship_fee,',.2f'),sep='')
        
    elif weight > 10:
         rate_per_kg = 3.80
         ship_fee = rate_per_kg * weight
         print("Rate per kg = $",format(rate_per_kg,',.2f'),sep='')
         print ("The shipping fee is $",format(ship_fee,',.2f'),sep='')
         
    else:
        print("Errorrrrr!!!! Bitch!")
        
        


main()