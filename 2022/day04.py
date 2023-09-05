'''
File: day04.py
Author: Jaro Hradsky
Date: 2023-09-06
Description: Original solution of https://adventofcode.com/2022/day/4
'''

day ='04'

sum1, sum2 = 0, 0
for line in open('input/' + day + '.txt'):
    line = line.strip() # remove new line chatacter from line end
    elf1, elf2 = line.split(',') # get sections range for each elf
    start1, end1 = map(int,elf1.split('-')) # get start and end section IDs as int for elf1
    start2, end2 = map(int,elf2.split('-')) # get start and end section IDs as int for elf2

    if (start2 >= start1) and (end2 <= end1) or (start1 >= start2) and (end1 <= end2): sum1 += 1 # Fully overlap
    if (start2 <= end1) and (start2 >= start1) or (start1 <= end2) and (start1 >= start2): sum2 += 1 # Partial overlap

print('Answer 1: ', sum1) # 2 | 595
print('Answer 2: ', sum2) # 4 | 952