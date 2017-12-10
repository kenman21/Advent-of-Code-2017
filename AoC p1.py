# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:58:00 2017

@author: Kenny
"""

'''
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next 
digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

'''
number = str(input('Enter any number: '))

i = 0
sum1 = 0 
sum2 = 0 
o = int(len(number)/2) 


for digit in range(len(number)) :
    if int(number[i]) == int(number[i-1]):
        sum1 = sum1 + int(number[i])
        i += 1 
    else : 
        i += 1 
    
i = 0 

for digit in range(len(number)) : 
    if i < o and int(number[i+o]) == int(number[i]):  
        sum2 = sum2 + int(number[i])
        i += 1
    elif i >= o and int(number[i-o]) == int(number[i]):
        sum2 = sum2 +int(number[i])
        i += 1
    else: 
        i += 1 
        
print('The sum from part 1 is: ', sum1)
print('The sum from part 2 is: ', sum2)