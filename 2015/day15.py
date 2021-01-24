import re
import random

from itertools import permutations

# Udelej vsecky 4 clenne permutace cisel 0-100 
lst = list()
for i in range(0,101): lst.append(i)
comb = permutations(lst,4)
clist = list(comb)


# Vyber jen ty co dohromady daji 100
list100 = list()
for c in clist: 
    if sum(c) == 100: list100.append(c)

# nacti input
ingredients = list()
for line in open("day15-input.txt"):
    s = re.findall("[-]*[0-9]+", line)
    ingredients.append(s)

max = 0
kmax = 0
for spoons in list100:
    total = 1
    for j in range(0,4): 
        sum = 0
        for i in range(len(spoons)):
            sum += int(ingredients[i][j]) * spoons[i]
        if sum < 0: sum = 0
        total *= sum
    ksum = 0
    for i in range(len(spoons)):
        ksum += int(ingredients[i][4]) * spoons[i]
    if total > max: max = total
    if ksum == 500 and total > kmax: kmax = total
print("Total score of the highest-scoring cookie:", max)
print("Total score of the highest-scoring cookie with 500 calories:", kmax)