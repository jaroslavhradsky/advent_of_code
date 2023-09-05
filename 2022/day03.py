'''
File: day03.py
Author: Jaro Hradsky
Date: 2023-09-05
Description: Original solution of https://adventofcode.com/2022/day/3
'''

day ='03'

def get_priority(item_type):
    if 'a' <= item_type <= 'z': return ord(item_type) - ord('a') + 1
    elif 'A' <= item_type <= 'Z': return ord(item_type) - ord('A') + 27
    else: return None

# Part 1 ------------------------------------------------------------------------------
sum1 = 0 
for line in open('input/' + day + '.txt'):
    items = line.strip() # Items in rucksack as string
    mid = len(items)//2
    first_compartment = list(items[:mid]) # 1st compartment as list of characters/items
    second_compartment = list(items[mid:]) # 2nd compartment as list of characters/items

    # Find common item, get priority and increase the sum
    for item in first_compartment:
        if item in second_compartment: common_item = item
    sum1 += get_priority(common_item) 

# Part 2 ------------------------------------------------------------------------------
sum2 = 0
with open('input/' + day + '.txt') as input:
    while True:
        rucksack1 = input.readline().strip()
        rucksack2 = input.readline().strip()
        rucksack3 = input.readline().strip()
        if not (rucksack1 or rucksack2 or rucksack3): break
        for ch in rucksack1:
            if ch in rucksack2 and ch in rucksack3: common_item = ch
        sum2 += get_priority(common_item)

print('Answer 1: ', sum1) # 7980
print('Answer 2: ', sum2) # 2881