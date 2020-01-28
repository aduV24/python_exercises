# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:44:12 2019

@author: NOTEBOOK
"""
#The main fuction gets the number of books purchased 
#and calls the points_earned function
def main():
    books = int(input('Enter number of books purchased :'))

    points_earned(books)
    
    # This function chcks the number of books,assigns and prints points as due
def points_earned(books):
    if books == 0:
        print('You have earned 0 points so far pls do well '+
               'to purchase books to get more points')
    elif books == 1:
         print('Congrats!! You have earned 5 points so far')
    elif books == 2:
        print('Congrats!! You have earned 15 points so far')
    elif books == 3:
        print('Congrats!! You have earned 30 points so far')
    elif books >= 4:
        print('Congrats!! You have earned the maximum 60 points')
    else:
        print('Erorrr!!')
        
           
            
            
            
main()
          