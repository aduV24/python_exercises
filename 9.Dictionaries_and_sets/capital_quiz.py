# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:03:35 2020

@author: NOTEBOOK
"""


def main():
    #Create dictionary
    capitals = {'Algeria':'Algiers',
                'Angola' :'Luanda',
                'Benin':'Porto-Novo',
                'Botswana':'Gaborone',
                'Burundi':'Bujumbura',
                'Burkina Faso':'Ouagadougou',
                'Cameroon':'Yaoundé',
                'Cape Verde':'Praia',
                'Central African Republic':'Bangui',
                'Chad':'N’Djamena',
                'Comoros':'Moroni',
                'DR Congo':'Kinshasa',
                'Djibouti':'Djibouti City',
                'Egypt':'Cairo',
                'NIgeria':'Abuja'
                }    
    print('Welcome to Capital quiz')
    print('Enter the capitals of the following countries')
    
    #Create a variable to control the loop
    again = 'y'
    
    #Initialize accumulators for correct and incorrect answers
    total_1 = 0
    total_2 = 0
   #Pick random from dict 
    while again == 'y':
        print('Enter the Capital of')
        country,cap = capitals.popitem()
        capital = input(country + str(': '))
        
       
        if capital == cap:
            print('Correct!')
            total_1 += 1
        else:
            print('Wrong,answer is', cap )
            total_2 += 1
        print()
        print('Do you wanna Continue')
        again =input('Enter y for yes, any key for no: ')
        print('----------------------------------')
    
        #Display results
    print('Total attempts: ',total_1 + total_2)
    print('Correct answers: ',total_1)
    print('Incorrect answers', total_2)
main()
            