# --- Day 11: Corporate Policy ---

# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

#     Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
#     Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
#     Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

# For example:

#     hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
#     abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
#     abbcegjk fails the third requirement, because it only has one double letter (bb).
#     The next password after abcdefgh is abcdffaa.
#     The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

# Given Santa's current password (your puzzle input), what should his next password be?

# Your puzzle answer was vzbxxyzz.
# --- Part Two ---

# Santa's password expired again. What's the next one?

# Your puzzle answer was vzcaabcc.

# Both parts of this puzzle are complete! They provide two gold stars: **

# At this point, you should return to your Advent calendar and try another puzzle.

# Your puzzle input was vzbxkghb.



def valid_pwd(pwd):
    valid = 0

    # Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz
    for i in range(len(pwd)-2):
        if (pwd[i])+1 == (pwd[i+1]) and (pwd[i])+2 == (pwd[i+2]): 
            valid += 1
            break

    # Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    if 8 not in pwd and 14 not in pwd and 11 not in pwd: 
        valid += 1

    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    pairs = list()
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1] and (pwd[i], pwd[i+1]) not in pairs:
            pairs.append((pwd[i], pwd[i+1]))
    if len(pairs) >= 2: 
        valid += 1

    if valid == 3: return True
    return False    


input = "vzbxxzaa"

pwd = list(input)
for i in range(len(pwd)):
    pwd[i] = ord(pwd[i]) - ord('a')

while not valid_pwd(pwd):
    tocim = True
    j = len(pwd)-1
    while tocim:
        pwd[j] = (pwd[j]+1) % 26
        if pwd[j] == 0:
            j -= 1
        else: tocim = False

result = ""
for i in range(len(pwd)): result += chr(pwd[i]+ord('a'))
print(result)