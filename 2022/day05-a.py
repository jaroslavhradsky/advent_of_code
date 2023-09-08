'''
File: day05-a.py
Author: Jaro Hradsky
Date: 2023-09-08
Description: ANother solution of https://adventofcode.com/2022/day/5 using 
    - zip() and unpacking operator to parse the drawing
    - slicing instead of .pop() and .append()
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

# Tranform lines to columns, * operator unpacks the list, 'zip' creates tupple generator from each column
columns = zip(*lines)

stacks = ['#'] # One empty stack, stack numbering starts at 1 as per instructions
for i, column in enumerate(columns):
    if i % 4 == 1: stacks.append(''.join(column[:-1]).lstrip()) # filter only useful columns, remove white spaces from the top of stack

# ['NZ', 'DCM', 'P'] here is how the stacks looks now

original_stacks = stacks[:] # Save the state for Part2

# Part1 -------------------------------------------------------

# Simulate the rearrangement procedure
for move_count, move_from, move_to in instructions:
    temp_stack = stacks[move_from][:move_count][::-1]
    stacks[move_from] = stacks[move_from][move_count:]
    stacks[move_to] = temp_stack + stacks[move_to]

top = ''.join([stack[0] for stack in stacks[1:]]) # get the final 'word' from the top crates of each stack
print('Answer 1: ', top) # 'CMZ' | 'TLNGFGMFN'

# Part2 -------------------------------------------------------
stacks = original_stacks
# Simulate the rearrangement procedure
for move_count, move_from, move_to in instructions:
    temp_stack = stacks[move_from][:move_count] # just remove [::-1] from Part1 so that the crates in move are not reversed
    stacks[move_from] = stacks[move_from][move_count:]
    stacks[move_to] = temp_stack + stacks[move_to]

top = ''.join([stack[0] for stack in stacks[1:]]) # get the final 'word' from the top crates of each stack
print('Answer 2: ', top) # 'MCD' | 'FGLQJCMBD'