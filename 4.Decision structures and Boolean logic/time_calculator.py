# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:25:50 2019

@author: NOTEBOOK
"""

def main():
    seconds = int(input("Enter number of seconds: "))
    if seconds >= 60 and seconds < 3600:
       time = seconds // 60
       print(time,"minutes")
       
    elif seconds >= 3600 and seconds < 86400 :
         time = seconds // 3600
         print(time,"Hours")
       
    elif seconds >=86400:
         time = seconds // 86400
         print(time,"Days")
    else: 
        print(seconds,"seconds")
main()