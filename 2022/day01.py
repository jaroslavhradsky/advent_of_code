'''
File: day01.py
Author: Jaro Hradsky
Date: 2023-09-04
Description: Original solution of https://adventofcode.com/2022/day/1
'''

day ='01'
input = open('input/' + day + '.txt')

elf_cal = 0
max_cal = 0
elves = []
for line in input:
    if line != '\n': # Add to current elf
        cal = int(line)
        elf_cal += cal
    else: # Stop calculation for current elf and check if maximum found
        if elf_cal > max_cal: max_cal = elf_cal
        elves.append(elf_cal)
        elf_cal = 0

# Process the last elf
if elf_cal > max_cal: max_cal = elf_cal
elves.append(elf_cal)

elves.sort(reverse=True)

print('Answer 1:',max_cal)  # 2400 | 66616
print('Answer 2:',elves[0]+elves[1]+elves[2]) # 45000 | 199172
