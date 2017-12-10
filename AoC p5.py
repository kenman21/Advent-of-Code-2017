# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:12:50 2017

@author: Kenny
"""

message = '0 3 0 1 -4'
message_list = message.split(' ')
i = 0
j = 0 
message_dict = {0:0}

for y in message_list:
    message_list[j] = int(message_list[j])
    message_dict[j] = message_list[j]
    j += 1

x = {0:0}

while x[i] < len(message_list) and x[i] >= 0:
    i += 1 
    x[i] = x[i-1] + message_dict[x[i-1]]
    message_dict[x[i-1]] += 1

position_list = list(x.values())
for position in position_list:
    if position >= len(message_list) or position < 0: 
        print('It took', position_list.index(position), 'steps to exit')