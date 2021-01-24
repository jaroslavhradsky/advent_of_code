# --- Day 16: Aunt Sue ---

# Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

# You have 500 Aunts named "Sue".

# So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

# The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

#     children, by human DNA age analysis.
#     cats. It doesn't differentiate individual breeds.
#     Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
#     goldfish. No other kinds of fish.
#     trees, all in one group.
#     cars, presumably by exhaust or gasoline or something.
#     perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

# In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1

# You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

# What is the number of the Sue that got you the gift?

# Your puzzle answer was 103.
# --- Part Two ---

# As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

# In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

# What is the number of the real Aunt Sue?

# Your puzzle answer was 405.


import re
aunts = list()

my_aunt = {"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}

for line in open("day16-input.txt"):
    
    things = re.findall("Sue .*?: (.*)", line)[0].split(",")
    aunt = dict()
    for t in things:
        key = t.split(":")[0].strip()
        val = int(t.split(":")[1].strip())
        aunt[key] = val
    aunts.append(aunt)

max = 0
susp_aunt = 1   
for i in range(0, 500):
    match = 0
    for key, val in my_aunt.items():
        if my_aunt[key] == aunts[i].get(key):
            match += 1
    if match > max:
        susp_aunt = i+1
        max = match
print("number of the Sue that got you the gift is:",susp_aunt)


max = 0
susp_aunt = 1   
for i in range(0, 405):
    match = 0
    for key, val in my_aunt.items():
        if key not in ["cats", "trees", "pomeranians", "goldfish" ]:
            if my_aunt[key] == aunts[i].get(key, -10): match += 1
        elif key in ["cats", "trees"]:
            if my_aunt[key] <= aunts[i].get(key,-10): match += 1
        else:
            if my_aunt[key] >= aunts[i].get(key, 99): match += 1

            
    if match > max:
        print(i+1, aunts[i], match)
        susp_aunt = i+1
        max = match
print("number of the Sue that got you the gift is:",susp_aunt)