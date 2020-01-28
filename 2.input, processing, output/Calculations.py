# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:21:40 2019

@author: NOTEBOOK
"""

print ("This program helps to Calculate you final year mark")

cr = int(input ("Enter your class record: "))

exam_mark = int(input("Enter your exam mark: "))

total_mark = int((0.7 * cr) + (0.3 * exam_mark))

print ("End of the year mark = ", total_mark)
