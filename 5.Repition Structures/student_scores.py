# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 00:08:46 2019

@author: NOTEBOOK
"""

def main():
    #Get the number of students and number of test scores
    num_students = int(input('Enter your number of students: '))
    num_test_scores = int(input('Enter number of test scores: '))
    #Determine each student average score
    for student in range (num_students):
        #Set accumulator to 0
        total = 0.0
        #Print Headings
        print ("Student number",student + 1)
        print ("----------------")
        #Get student test score
        for test_scores in range (num_test_scores):
            score = float(input("Test number" + str(test_scores + 1) +": "))
            # Add test score to accumulator
            total += score
            #Calculate average test score
        average = total / num_test_scores
            #Display total and average test score
        print ("Total for stundent number",student + 1,"is:", total)
        print ("Average for stundent number",student + 1,"is:", format(average,'.2f'))
        print ()
main()