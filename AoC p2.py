# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:26:16 2017

@author: Kenny
"""
'''
The spreadsheet consists of rows of apparently-random numbers. To make sure the
 recovery process is on the right track, they need you to calculate the spreadsheet's checksum. 
For each row, determine the difference between the largest value and the smallest value; the 
checksum is the sum of all of these differences.

'''

q1 = input('Enter the first row of the spreadsheet: ')
q2 = input('Enter the second row of the spreadsheet: ')
q3 = input('Enter the third row of the spreadsheet: ')

row1 = [0]*len(q1)
row2 = [0]*len(q2)
row3 = [0]*len(q3)

i = 0
j = 0
k = 0 

for number in row1: 
    row1[i] = q1[i]
    i += 1
    
for number in row2: 
    row2[j] = q2[j]
    j += 1
    
for number in row3: 
    row3[k] = q3[k]
    k += 1
    
sum1 = int(max(row1)) - int(min(row1))
sum2 = int(max(row2)) - int(min(row2))
sum3 = int(max(row3)) - int(min(row3))

checksum = sum1 + sum2 + sum3

print('The checksum is equal to :', checksum)