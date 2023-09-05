'''
File: day03.py
Author: Jaro Hradsky
Date: 2023-09-05
Description: Another solution of https://adventofcode.com/2022/day/3. One loop through input file. No need to convert line/string to list of chars
'''

day ='03'

def get_priority(item_type):
    if 'a' <= item_type <= 'z': return ord(item_type) - ord('a') + 1
    elif 'A' <= item_type <= 'Z': return ord(item_type) - ord('A') + 27
    else: return None

sum1, sum2 = 0, 0
group = []
for line in open('input/' + day + '.txt'):
    line = line.strip()
    mid = len(line)//2
    first_compartment, second_compartment = line[:mid], line[mid:]

    # Find common item, get priority and increase the sum
    for item in first_compartment:
        if item in second_compartment: 
            sum1 += get_priority(item)
            break
    
    group.append(line)

    if len(group) == 3:
        rucksack1, rucksack2, rucksack3 = group
        group = []
        for item in rucksack1:
            if item in rucksack2 and item in rucksack3: 
                sum2 += get_priority(item)
                break

print('Answer 1: ', sum1) # 7980
print('Answer 2: ', sum2) # 2881