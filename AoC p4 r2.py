# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:07:13 2017

@author: Kenny
"""

passphrase =  'aa a aad dab dd kenny ynnek'
passphrase_list = passphrase.split(' ')
invalid_phrase = 0
passphrase_copy = passphrase_list[:]


for phrases in passphrase_list: 
    if len(passphrase_copy) == 1:
        break
    del(passphrase_copy[0])
    for phrases2 in passphrase_copy:
        if len(phrases) != len(phrases2):
            continue
        phrases = ''.join(sorted(phrases)) 
        phrases2 = ''.join(sorted(phrases2))
        if phrases != phrases2:
            continue
        invalid_phrase += 1
        break
    else: 
        continue
    break
        
            
if passphrase_copy == 1:
    print('The passphrase is valid. ')
elif invalid_phrase == 1:
    print('You typed in an invalid passphrase. ')
else:
    print('You typed in an invalid passphrase. ')