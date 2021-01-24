# --- Day 17: No Such Thing as Too Much ---

# The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

#     15 and 10
#     20 and 5 (the first 5)
#     20 and 5 (the second 5)
#     15, 5, and 5

# Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

# Your puzzle answer was 1638.
# --- Part Two ---

# While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

# Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

# In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

# Your puzzle answer was 17.

from itertools import combinations  

containers = list()
for line in open("day17-input.txt"):
    containers.append(int(line.strip()))

#containers = [20, 15, 10, 5, 5]
liters = 150

print(containers)
count = 0
found = False
mincount = 0
for length in range (1,len(containers)+1):
    for c in combinations(containers,length):
        if sum(c) == liters:
            count += 1
            if not found:
                found = True
                mincount = length 
print("Number of different combinations to fit:", count)


count = 0
for c in combinations(containers,mincount):
    if sum(c) == liters:
        count += 1
print("Number of different combinations with minimum containers:", count)

