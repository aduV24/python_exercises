# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:52:52 2020

@author: NOTEBOOK
"""

def main():
   ''' num = int(input('Enter a number: '))

  
# Driver Program  
    if isPrime(num): 
        print ("true") 
    else: 
        print ("false") 
        
        
def isPrime(num): 
       # Corner case 
       if (num <= 1): 
            return False
      
        # Check from 2 to n-1 
       for i in range(2, num): 
            if (num % i == 0): 
                print(i)
                return False
  
       return True'''
   for num in range (2,101):
           if is_prime(num):
               print(num)
       
def is_prime(num):
    for i in range(2, num): 
            if (num % i == 0): 
                return False
  
    return True
             
            
        
main()
