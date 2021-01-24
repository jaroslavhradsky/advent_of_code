# --- Day 3: Squares With Three Sides ---

# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

# Or are they?

# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

# In your puzzle input, how many of the listed triangles are possible?

# Your puzzle answer was 917.
# --- Part Two ---

# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603

# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

# Your puzzle answer was 1649.


count = 0
for line in open("day03-input.txt"):
    s = line.strip().split()
    for i in range(len(s)):
        s[i] = int(s[i])
    if s[0]+s[1] > s[2] and s[1]+s[2] > s[0] and s[0]+s[2] > s[1]: count += 1
print("Number of valid triangles:",count)



count = 0
triangle = list()
for n in range(0,3):
    for line in open("day03-input.txt"):   
        triangle.append(int(line.strip().split()[n]))
        if len(triangle) == 3:
            if triangle[0]+triangle[1] > triangle[2] and triangle[1]+triangle[2] > triangle[0] and triangle[0]+triangle[2] > triangle[1]: count += 1
            triangle = list()
print("Number of valid triangles:",count)
