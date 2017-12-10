# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:16:31 2017

@author: Kenny
"""
import math
memory_bank = input('Enter in the memory bank: ')
memory_bank_list = memory_bank.split(' ')

i = 0 
j = 0
k = 0
check_value = 0 

for y in memory_bank_list:
    memory_bank_list[k] = int(memory_bank_list[k])
    k += 1
    
memory_bank_dict = {0: memory_bank_list}
#
while check_value != 1 :
    reall = max(memory_bank_dict[i])/len(memory_bank_dict[i])
    memory_bank_copy = memory_bank_dict[i]
    memory_bank_list = memory_bank_copy[:]
    memory_bank_record = memory_bank_copy[:]
    for j in range(0, len(memory_bank_list)):
        if j == memory_bank_record.index(max(memory_bank_record)):
            memory_bank_list[j] = math.floor(reall)
            continue
        memory_bank_list[j] = memory_bank_list[j] + math.ceil(reall)
    if memory_bank_list in list(memory_bank_dict.values()):
        check_value = 1
        break
    memory_bank_dict[i+1] = memory_bank_list
    i += 1
    
print('The answer is: ',i+1)