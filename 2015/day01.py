'''
File: day01.py
Author: Jaro Hradsky
Date: 2023-09-11
Description: Original solution of https://adventofcode.com/2015/day/1
'''

day ='01'

input = open('input/' + day + '.txt').read()

floor = 0
basement = False
for i in range(0, len(input)):
    if input[i] == "(": floor += 1
    else: floor -= 1
    if floor < 0 and not basement: 
        basement = True
        print('Answer 2: ', i+1) 

print('Answer 1:', floor)