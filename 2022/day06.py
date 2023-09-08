'''
File: day06.py
Author: Jaro Hradsky
Date: 2023-09-08
Description: Original solution of https://adventofcode.com/2022/day/6
'''
day ='06'

buffer = open('input/' + day + '.txt').read()

# Part 1 -----------------------------------------------------------
for i in range(4,len(buffer)):
    four = buffer[i-4:i]
    if all([four.count(character) == 1 for character in four]):
        answer1 = i
        break
    
# Part 2 -----------------------------------------------------------
for i in range(14,len(buffer)):
    fourteen = buffer[i-14:i]
    if all([fourteen.count(character) == 1 for character in fourteen]):
        answer2 = i
        break

print('Answer 1: ', answer1) # 7 | 1300
print('Answer 2: ', answer2) # 19 | 3986