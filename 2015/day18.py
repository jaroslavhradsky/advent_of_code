# --- Day 18: Like a GIF For Your Yard ---
# After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.
# Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.
# Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".
# Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".
# For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

# 1B5...
# 234...
# ......
# ..123.
# ..8A4.
# ..765.

# The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:
#     A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
#     A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
# All of the lights update simultaneously; they all consider the same current state before moving to the next.

# Here's a few steps from an example configuration of another 6x6 grid:
# Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..

# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..

# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....

# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......

# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......

# After 4 steps, this example has four lights on.
# In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
# Your puzzle answer was 1061.


# --- Part Two ---
# You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

# Initial state:
# ##.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####.#

# After 1 step:
# #.##.#
# ####.#
# ...##.
# ......
# #...#.
# #.####

# After 2 steps:
# #..#.#
# #....#
# .#.##.
# ...##.
# .#..##
# ##.###

# After 3 steps:
# #...##
# ####.#
# ..##.#
# ......
# ##....
# ####.#

# After 4 steps:
# #.####
# #....#
# ...#..
# .##...
# #.....
# #.#..#

# After 5 steps:
# ##.###
# .##..#
# .##...
# .##...
# #.#...
# ##...#

# After 5 steps, this example now has 17 lights on.
# In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?
# Your puzzle answer was 1006.


from time import sleep
from os import system
from copy import deepcopy
import matplotlib.pyplot as plt

m = list()
m.append([0]*102)
for line in open("day18-input.txt"):
    row = list()
    row.append(0)
    for ch in line.strip():
        if ch == "#": row.append(1)
        else: row.append(0)
    row.append(0)
    m.append(row)
m.append([0]*102)


plt.ion()
for step in range(0,101):

    # for part2 only
    # m[1][1] = 1
    # m[1][100] = 1
    # m[100][1] = 1
    # m[100][100] = 1

    sum1 = 0
    for row in m[0:101]: sum1 += sum(row)
    print("Step:",step, "Lights:",sum1)

    new_m = deepcopy(m) #musim pouzit deepcopy, protoze jinak mi to zkopituje jen odkazy na list a ne cisla
    for row in range(1,101):
        for column in range(1,101):
            suma = 0
            for r in range(row-1, row+2):
                for c in range(column-1, column+2):
                    suma += m[r][c]
            suma = suma - m[row][column]

            if m[row][column] == 1:
                if (suma != 2 and suma != 3): 
                    new_m[row][column] = 0
            else:
                if (suma == 3): 
                    new_m[row][column] = 1
    m = deepcopy(new_m)



    plt.imshow(m, cmap='gray', interpolation='none')
    plt.savefig(str(step) + ".png")
