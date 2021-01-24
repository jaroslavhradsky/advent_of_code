# --- Day 21: RPG Simulator 20XX ---

# Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

# In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

# Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

# Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

# Here is what the item shop is selling:

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

# You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

# For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

#     The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
#     The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
#     The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
#     The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
#     The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
#     The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
#     The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.

# In this scenario, the player wins! (Barely.)

# You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

# Your puzzle answer was 91.
# --- Part Two ---

# Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

# What is the most amount of gold you can spend and still lose the fight?

# Your puzzle answer was 158.

import random

weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
armors = [(13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
rings = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]

min_cost = 999
max_cost = 0
for i in range(1,5000):
    boss_points = 100
    boss_damage = 8
    boss_armor = 2


    # Select weapon
    weapon = random.choice(weapons)
    me_damage = weapon[1]
    cost = weapon[0]

    # Select armor
    armor = (0,0,0)
    if random.choice([True, False]):
        armor = random.choice(armors)
    #print("Armor:", armor)
    me_armor = armor[2]
    cost += armor[0]

    # Select ring(s)
    r = random.randint(0,2)
    if r == 1:
        chosen_rings = list()
        chosen_rings.append(random.choice(rings))
    if r == 2:
        chosen_rings = random.sample(rings,2)
    if r == 0:
        chosen_rings = list()

    for r in chosen_rings:
        me_damage += r[1]    
        me_armor += r[2]
        cost += r[0]


    
    me_points = 100
    #print("Cost: %3d Damage: %2d Armor: %2d" % (cost, me_damage, me_armor), end="    ")
    turn = 1

    # Fight
    while boss_points > 0 and me_points > 0:
        if turn % 2 == 1:
            me_atack = me_damage - boss_armor
            if me_atack < 1: me_atack = 1
            boss_points -= me_atack
            #print("%3d    me: %2d    ->    boss %2d" % (turn, me_points, boss_points))

        else:
            boss_atack = boss_damage - me_armor
            if boss_atack < 1: boss_atack = 1
            me_points -= boss_atack
            #print("%3d    me: %2d    <-    boss %2d" % (turn, me_points, boss_points))
        turn += 1
    if boss_points > 0: 
        #print("Boss won")
        if cost > max_cost: max_cost = cost
    else: 
        if cost < min_cost: min_cost = cost
        #print("You won !!!")
print()
print("The least amount of gold you can spend and still win the fight:", min_cost)
print("The most amount of gold you can spend and still lose the fight", max_cost)