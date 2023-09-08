'''
File: day05.py
Author: Jaro Hradsky
Date: 2023-09-06
Description: Original solution of https://adventofcode.com/2022/day/5
'''
import re

day ='05'

# Read drawing of the starting stacks of crates and the rearrangement procedure 
drawing, procedure = open('input/' + day + '.txt').read().split('\n\n')

# Load instructions. Whole procedure is saved in list of tuples. Each tuple is a line in rearrangement procedure
instructions = []
for line in procedure.split('\n'): # in each line
    instruction = tuple(map(int,re.findall(r'\b\d+\b',line))) # find all numbers surrounded by characters, convert number strings to integer and create tuple (with 3 values)
    instructions.append(instruction) # append to a list of instructions

# Load stacks
lines = []
for line in drawing.split('\n'):
    lines.append(line) 
length = len(lines[0])

# Convert input columns to list of characters
# 'line[i] for line in lines' is one letter in column
# 'line[i] for line in lines][::-1] for i in range(length)' do that for each letter in a column
# '[[line[i] for line in lines][::-1] for i in range(length)]' and return it in reverse order
# '[stack for stack in [[line[i] for line in lines][::-1] for i in range(length)] if stack[0].isdigit()]' and only for columns containing number at the bottom
stacks1 = [stack for stack in [[line[i] for line in lines][::-1] for i in range(length)] if stack[0].isdigit()]

# FInish the stack initialization so it looks like [['Z','N'],['M','C','D'],['P']] for test input
for i in range(len(stacks1)):
    new_stack = [char for char in stacks1[i] if char != ' '][1:] # Remove spaces from the top of stack and remove a number from the bottom
    stacks1[i] = new_stack

stacks2 = [stack[:] for stack in stacks1] # Part2 copy of stacks. I cannot use stacks1.copy() or stacks1[:] as it creates a shallow copy, where inner lists still reference the same objects 

# Simulate the rearrangement procedure
for instruction in instructions:
    move_count = instruction[0]
    move_from = instruction[1] - 1
    move_to = instruction[2] - 1
    
    temp_stack = [] # Part 2
    for i in range(move_count):
        crate = stacks1[move_from].pop() # remove from stack
        stacks1[move_to].append(crate) # add to stack
        
        crate = stacks2[move_from].pop() # remove from stack        
        temp_stack.append(crate) # Part 2: add crate to temp stack

    for i in range(move_count): stacks2[move_to].append(temp_stack.pop()) # Part2: Move the crates to detination stack in the correct order

top1 = ''.join([stack[-1] for stack in stacks1]) # get the final 'word' from the top crates of each stack
top2 = ''.join([stack[-1] for stack in stacks2]) # get the final 'word' from the top crates of each stack

print('Answer 1: ', top1) # 'CMZ' | 'TLNGFGMFN'
print('Answer 2: ', top2) # 'MCD' | 'FGLQJCMBD'