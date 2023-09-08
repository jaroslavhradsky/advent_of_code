'''
File: day06.py
Author: Jaro Hradsky
Date: 2023-09-08
Description: Another solution of https://adventofcode.com/2022/day/6 using set and function
'''
day ='06'

buffer = open('input/' + day + '.txt').read()

# Length is length of substring that should not contain same characters. Therefore we start after first 'lenght' of characters. 
# set() ensures characters don't repeat. So if set() size is same as size of initial substring, we did find the susbtring with non-repeating characters
def get_start(buffer, length):
    for i in range(length,len(buffer)):
        if len(set(buffer[i-length:i])) == length:
            return i
    return None

print('Answer 1: ', get_start(buffer,4)) # 7 | 1300
print('Answer 2: ', get_start(buffer,14)) # 19 | 3986