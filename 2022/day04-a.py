'''
File: day04.py
Author: Jaro Hradsky
Date: 2023-09-05
Description: Another solution of https://adventofcode.com/2022/day/4 using sets
'''

day ='04'

sum1, sum2 = 0, 0
for line in open('input/' + day + '.txt'):
    line = line.strip() # remove new line chatacter from line end
    elf1, elf2 = line.split(',') # get sections range for each elf
    start1, end1 = map(int,elf1.split('-')) # get start and end section IDs as int for elf1
    start2, end2 = map(int,elf2.split('-')) # get start and end section IDs as int for elf2

    sections1 = set(range(start1, end1 + 1))
    sections2 = set(range(start2, end2 + 1))

    overlap = sections1 & sections2 # Intersection is partial overlap
    if overlap: # If intersection exists, then there is Partial overlap
        sum2 += 1
        if sections1 <= sections2 or sections2 <= sections1: sum1 += 1 # If first set is fully included in second one or vice versa, there is Full overlap

print('Answer 1: ', sum1) # 2 | 595
print('Answer 2: ', sum2) # 4 | 952