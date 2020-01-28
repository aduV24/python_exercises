# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:45:30 2019

@author: NOTEBOOK
"""

wages = float(input('Wages :'))
tax = wages * 0.157 
print("The tax due is $",
      format(tax, ',.2f'), sep='')
print ("The tax in percentage is ", format(0.157,'.1%'))