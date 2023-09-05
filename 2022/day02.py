'''
File: day02.py
Author: Jaro Hradsky
Date: 2023-09-04
Description: Solution of https://adventofcode.com/2022/day/2
'''

day ='02'

#Q1
# A, X is Rock, score 1
# B, Y is Paper, score 2
# C, Z is Scissors, score 3

# outcome_score = 0 if loss, 3 if draw, 6 if win
# round_score = shape_score + outcome_score

# All score combinations Q1
round_score1 = {
    'A X': 1 + 3, # Rock/Rock + Draw
    'A Y': 2 + 6, # Rock/Paper + Win
    'A Z': 3 + 0, # Rock/Scissors + Loss
    'B X': 1 + 0, # Paper/Rock + Loss
    'B Y': 2 + 3, # Paper/Paper + Draw
    'B Z': 3 + 6, # Paper/Scissors + Win
    'C X': 1 + 6, # Scissors/Rock + Win
    'C Y': 2 + 0, # Scissors/Paper + Loss
    'C Z': 3 + 3, # Scissors/Scissors + Draw
}

with open('input/' + day + '.txt') as input:
     score1 = sum(round_score1[round] for round in input.read().split('\n'))

#Q2
# X is Loss
# Y is Draw
# Z is Win

# All score combinations Q2
round_score2 = {
    'A X': 3 + 0, # Rock/Scisors + Loss
    'A Y': 1 + 3, # Rock/Rock + Draw
    'A Z': 2 + 6, # Rock/Paper + Win
    'B X': 1 + 0, # Paper/Rock + Loss
    'B Y': 2 + 3, # Paper/Paper + Draw
    'B Z': 3 + 6, # Paper/Scissors + Win
    'C X': 2 + 0, # Scissors/Paper + Loss
    'C Y': 3 + 3, # Scissors/Scissors + Draw
    'C Z': 1 + 6, # Scissors/Rock + Win
}

with open('input/' + day + '.txt') as input:
     score2 = sum(round_score2[round] for round in input.read().split('\n'))

print('Answer 1:',score1)
print('Answer 2:',score2)



    
