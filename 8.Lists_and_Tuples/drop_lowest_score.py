# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:58:56 2020

@author: NOTEBOOK
"""
# This program gets a series of test scores and
# calculates the average of the scores with the
# lowest score dropped.

def main():
  #Create a blank list
    scores =[]
  #Create a variable to control the loop  
    again = 'y'
   #Add scores to the list
    while again == 'y':
        score = int(input('Enter a test score: '))
        scores.append(score)
        print('Do you wanna add another score?')
        again = input('y for yes, anything for no: ')
    
    new_scores = drop_lowest_score(scores)    
  #Initialize accumulator
    total = 0.0
    
    #Calculate and display total and average 
    for index in range(len(new_scores)):
        total += new_scores[index]
    print()
    print('The total Scores Excluding the lowest one is: ',\
          format(total,',.2f'),sep='')
    avg = total/len(new_scores)
    print('The Average Excluding the lowest one is: ',\
          format(avg,',.2f'),sep='')
         
        
 #This function gets a list, removes the lowst score
 #And returnes a new list without the score
def drop_lowest_score(list):
    lowest = min(list)
    list.remove(lowest)
    return list
    
main()