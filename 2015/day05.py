# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

# Your puzzle answer was 258.
# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:

#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?

# Your puzzle answer was 53.

# Question 1
wovels = "aeiou"
naughty_strings = ["ab", "cd", "pq", "xy"]
count = 0
for line in open("day05-input.txt"):
    wcount = 0
    prev_ch = ""
    repeat = False
    for ch in line:
        if ch in wovels: wcount += 1
        if ch == prev_ch: repeat = True
        prev_ch = ch
    naughty = False
    for str in naughty_strings:
        if str in line: naughty = True
    if wcount >= 3 and repeat and not naughty: count += 1
print("Number of nice strings:", count)

# Question 2
count = 0
for line in open("day05-input.txt"):
    pair_cond = False
    for i in range(0,len(line)-1):
        pair = line[i]+line[i+1]
        if pair in line[i+2:]:
            pair_cond = True
            break
    middle_cond = False
    for i in range(1,len(line)-1):
        if line[i-1] == line[i+1]: middle_cond = True
    if pair_cond and middle_cond: 
        count += 1
print("Number of nice strings:", count)

