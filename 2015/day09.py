from itertools import permutations

locations = list()
distances = dict()
for line in open("day09-input.txt"):
    s = line.strip().split()
    loc = s[0]
    loc2 = s[2]
    distance = int(s[4])
    distances[loc+loc2] = distance
    distances[loc2+loc] = distance
    if not loc in locations: locations.append(loc)
    if not loc2 in locations: locations.append(loc2)

perm = permutations(locations,len(locations))
min = 9999999
max = 0
for path in list(perm): 
    dist = 0
    for i in range(0,len(path)-1):
        dist += distances[path[i]+path[i+1]]
    if dist < min: min = dist
    if dist > max: max = dist

print("Distance of shortest route is: ", min)
print("Distance of longest route is: ", max)