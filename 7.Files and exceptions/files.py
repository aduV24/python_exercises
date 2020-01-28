# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:53:54 2020

@author: NOTEBOOK
"""
def main():
    name1 = input('Name 1 please:')
    name2 = input('Name 2 please:')
    infile = open(r'C:\Python projects\files\catss.txt','a')
    infile.write(name1 + '\n')
    infile.write(name2 + '\n')
    infile.close()
    infile = open(r'C:\Python projects\files\catss.txt','r')
    print(infile.read())
    infile.close()
   
    
    

    
    
main()