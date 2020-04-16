# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:38:42 2020

@author: NOTEBOOK
"""
#This program uses dictionary to display
#course’s room number, instructor, and meeting time using the course code

def main():
    #Create dictionary
    room = {'CS101':'3004',
           'CS102':'4501',
           'CS103':'6755',
           'NT110':'1244',1     `                               ````````````````    `       
           'CM241':'1411'}
   
    instructor ={'CS101':'Hayness',
                 'CS102':'Alvaro',
                 'CS103':'Rich',
                 'NT110':'Burke',
                 'CM241':'Lee'}
    time = {'CS101':'8:00 a.m.',
           'CS102':' 9:00 a.m.',
           'CS103':' 10:00 a.m.',
           'NT110':' 11:00 a.m.',
           'CM241':' 1:00 p.m.'}
    
    print('Here are coursecodes:CS101,CS102,CS103,NT110,CM241')
    print('Choose a coursecode to scheduke a meeting')
    code = input('Enter Coursecode: ')
    
    print()
    print('Here are the details of your meeting')
    print('--------------------------------------')
    print('Room number:',room.get(code,'the code you entered is invalid'))
    print('instructor:',instructor.get(code,'the code you entered is invalid'))
    print('Time:',room.get(time,'the code you entered is invalid'))
main()

