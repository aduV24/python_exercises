# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:07:12 2020

@author: NOTEBOOK
"""

import os
new = open ('cofee.txt','w')
new.write('my name')
new.close()
print ('yes')
input('')
os.remove('cofee.txt')
print('Done')
