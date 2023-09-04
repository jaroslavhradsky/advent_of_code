'''
File: day01.py
Author: Jaro Hradsky
Date: 2023-09-04
Description: Advanced solution of https://adventofcode.com/2022/day/1
'''

day ='01'

with open('input/s' + day + '.txt') as input:
    elves = [sum(map(int,elf.split())) for elf in  input.read().split('\n\n')]

'''
1. input.read().split('\n\n') # List of strings (i.e. '7000\n8000\n9000'). One list item is one elf. 
2. [elf.split() for elf in  input.read().split('\n\n')] # List of lists (i.e ['7000', '8000', '9000']) of calories as strings
3. [sum(map(int,elf.split())) for elf in  input.read().split('\n\n')] # List of total calories per elf
'''

print('Answer 1:',max(elves))
print('Answer 2:',sum(sorted(elves,reverse=True)[0:3]))

'''
1. sorted(elves,reverse=True) # Return list sorted in descent order. We cannot use elves.sort() as it sorts the original list and returns None
2. sorted(elves,reverse=True)[0:3] # list slice of top 3 items
3. sum(sorted(elves,reverse=True)[0:3]) # Sum of top 3 values as required in the question
'''
