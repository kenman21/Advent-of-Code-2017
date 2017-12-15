# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:54:02 2017

@author: Kenny
"""

import operator 

with open('inputp8.txt') as f: 
    input_list = []
    for line in f: 
        input_list.append(line.split(" "))
        
# Take inputs from .txt, parse into list

for rows in input_list:
    for i in range(len(rows)):
        try: 
            rows[i] = int(rows[i])
        except ValueError: 
            pass

# Will need the numbers in the list to be integer values instead of strings so they can be fed into functions later


OPERATORS = {
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
}

# Create dictionary with boolean expressions

a = 0 
b = 0 

def inc(a,b):
    sum = a + b 
    return sum

def dec(a,b):
    diff = a - b
    return diff

registers_dict = {row[0]: 0 for row in input_list}
allregisters_list = []

# Create a dictionary with the registers as keys and their starting values as the values. Create another list to store 
# the results of each register operation
        
for line in input_list: 
    if OPERATORS[line[5]](registers_dict[line[4]],line[6]): 
        if line[1] == 'inc':
            sum = inc(registers_dict[line[0]], line[2])
            registers_dict[line[0]] = sum
            allregisters_list.append(sum)
        if line[1] == 'dec':
            diff = dec(registers_dict[line[0]], line[2])
            registers_dict[line[0]] = diff
            allregisters_list.append(diff)
    else: 
        continue
    
final_registers = list(registers_dict.values())
print('The max register value is %s' %max(final_registers))
print('The max register value held at any time is %s' %max(allregisters_list))



