# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:25:40 2020

@author: NOTEBOOK
"""
import pyperclip
import pprint
#Get the string to be counted from the clipboard
message = pyperclip.paste()
#Create an empty dictionary
count = {}
#COunt the string
for character in message.lower():
    count.setdefault(character,0)
    count[character] += 1
#initialize accumulator    
    total = 0
for i in count.values():
    total += i
#Display the string and frequency
pprint.pprint(count)
print()
print('Total amount of characters is ' ,total)
