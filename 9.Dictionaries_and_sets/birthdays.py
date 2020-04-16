# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:43:39 2020

@author: NOTEBOOK
"""


# This program uses a dictionary to keep friends’
# names and birthdays.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
   #Create an empty dictionary
   birthdays ={}
   choice = 0
   while choice != QUIT:
       choice = get_menu_choice()
           
       #Process the choice
       if choice == LOOK_UP:
           look_up(birthdays)
       elif choice == ADD:
           add(birthdays)
       elif choice == CHANGE:
           change(birthdays)
       elif choice == DELETE:
           delete(birthdays)
           
         

def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()    
   
    #Get the user's choice
    choice = int(input('Enter Valid Choice: '))
    
    # Validate choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter Valid Choice: '))
         
    return choice

def look_up(birthdays):
    #Get the name to look up
    name = input('Enter name to look up: ')
    
    #Check
    print(birthdays.get(name, 'Not found.'))
        
def add(birthdays):
   #Get name
    name = input('Enter name: ')
    b_day = input('Enter birthday: ')
    #CHeck if name isn't there already 
    if name not in birthdays:
        birthdays[name] = b_day
    else:
        print('That entry already exists.')
        
def change(birthdays):
   #Get name to lookup
    name = input('Enter a name:')
    #Update entry
    if name in birthdays:
        b_day = input('Enter birthday: ')
        birthdays[name] = b_day
    else:
        print('Name not found')
        
        
def delete(birthdays):
     #Get name to lookup
    name = input('Enter a name:')
    #Update entry
    if name in birthdays:
       del birthdays[name]
       print('Borthday has been deleted succesfully')
    else:
        print('Name not found')
    
        
main() 