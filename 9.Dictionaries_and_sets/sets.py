# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:40:32 2020

@author: NOTEBOOK
"""

 # This program demonstrates various set operations.
def main():
   #Create sets for both teams
   baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
   basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
   #Display names of people in the baseball team
   print('The following are names of people on the baseball team:')
   for name in baseball:
       print(name)
   print()
    #Display names of people in the basketball team    
   print('The following are names of people in the basketball team:')
   for name in basketball:
       print(name)
   print()
   # Demonstrate intersection       
   print('The following students play both basketball and baseball:')
   for name in baseball & basketball:
       print(name)
   print()
   #Demonstrate Union
   print('The following students play either baseball or basketball:')
   for name in baseball|basketball:
       print(name)
   print()
   #Demonstrate
   print('The following students play baseball but not basketball:')
   for name in baseball-basketball:
       print(name)
   print()
   #Demonstrate differnce
   print('The following students play basketball but not baseball:')
   for name in basketball-baseball:
       print(name)
   print()
   #Demonstrate systematic differnce
   print('The following students play one sport but not both:')
   for name in basketball^baseball:
       print(name)
   print('')
   
main()
   
  
   