# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:57:54 2020

@author: NOTEBOOK
"""
# This program displays test grades and average
from modules import average
from modules import grade


def main():
    #Initialize accumulator
    score = 0
    total = 0.0
    for num in range(5):
        #Get score and display grade
            score = int(input('Enter Score'+ ' ' + str(num+1) +': '))
            print ('Grade:', grade.det_grade(score))
            total+=score
    print()
    #Display Average
    print('Average is',average.cal_average(total))
    
    
main()
    
    