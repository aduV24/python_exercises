# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:10:32 2020

@author: NOTEBOOK
"""
#This program demonstrates how to use the index method
def main():
    # Create a list with some items.
    food = ['Pizza', 'Burgers', 'Chips']
    # Display the list.
    print('Here are the items in the food list:')
    print(food)
    #get the item to change
    item = input('Which Item should I change: ')
    try:
        item_index = food.index(item)
        new_item = input('What should it be replaced with?: ')
        food[item_index] = new_item
        # Display the list.
        print('Here is the revised list:')
        print(food)
    except ValueError:
        print('That item was not found in the list.')

              
main()