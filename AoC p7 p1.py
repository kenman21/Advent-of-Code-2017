# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:00:29 2017

@author: Kenny
"""
with open('inputp7.txt') as f: 
    input_list = []
    for line in f: 
        input_list.append(line.split(" "))

parentschildren_dict = {}
parents_list = []
childrens_list = []
grandparents_list = []
secondgen_list = []
     
for row in input_list: 
    i = 0
    for item in row: 
       for char in item: 
           if char.isalpha() == False:
               item = item.replace(char,"")
       row[i] = item
       i += 1
       
# Super shitty parsing of the the input, but it works I guess...would split the row to get rid of the arrow next time    
       
    if len(row) > 2: 
        parentschildren_dict[row[0]] = row[3:]
        parents_list.append(row[0])
        childrens_list.append(row[3:])
        
#The longer rows contain the children of the program...Throw the parents and children into seperate lists, and create a dictionary 
#so I can list out all of the first gen program's children in one go later on...

childrens_list = [y for x in childrens_list for y in x]

#Turn list of lists into one list

for parents in parents_list: 
    if parents not in childrens_list: 
            grandparents_list.append(parents)
    else: 
            secondgen_list.append(parents)

# If a parent is not in my children's list, then it must be the 'grandparent'

print(grandparents_list)
print(secondgen_list)
for secondparents in secondgen_list:
    print(parentschildren_dict[secondparents])

   
       