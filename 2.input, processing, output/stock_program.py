# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:24:47 2019

@author: NOTEBOOK
"""

#Buying of Shares

s_cp = float(input("How much is the share :"))
t_s = int(input("Total number of shares bought: "))
cp = s_cp * t_s
comm = 0.02 * cp
total = cp + comm
print("Cost Of Shares = ", format(cp, ',.2f'))
print("Agent's commission = ", format(comm, ',.2f'))
print("Total Cost  = ", format(total, ',.2f'))

# Sales of shares

s_sp = float(input("How much was it sold for :"))
t_ss = int(input("Total number of shares sold: "))
sp = s_sp * t_ss
commm = 0.02 * sp
totall = sp - comm
print("Sales Of Shares = ", format(sp, ',.2f'))
print("Agent's commission = ", format(commm, ',.2f'))
print("Total Sales  = ", format(totall, ',.2f'))


#Profit or loss####
p_l = totall - total
print("money left with you = ",format(p_l,',.2f'))