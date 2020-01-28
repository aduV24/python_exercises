# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:51:27 2020

@author: NOTEBOOK
"""
#This function determines the grade of each score
def det_grade(score):
    if score >= 90 and score <= 100:
        return 'A'
    elif  score >= 80 and score <= 89:
        return 'B'
    elif  score >= 70 and score <= 79:
        return 'C'
    elif  score >= 60 and score <= 69:
        return 'D'
    else:
        return 'F'