# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:49:48 2020

@author: NOTEBOOK
"""
from modules import k_energy
#This program calculates the kinetic energy
def main():
    mass = float(input('Enter mass of object:'))
    velocity = float(input('Enter velocity of object:'))
    print('Kinetic Energy is' , k_energy.kinetic_energy(mass,velocity))
    
main()

'''import sys
print(sys.path)'''