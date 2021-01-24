class Reindeer:
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = int(speed)
        self.time = int(time)
        self.rest = int(rest)
        self.distance = 0
        self.points = 0

    def print(self):
        print(self.name, self.speed, self.time, self.rest, self.distance, self.points)


reindeers = list()
for line in open("day14-input.txt"):
    s = line.strip().split()
    r = Reindeer(s[0], s[3], s[6], s[13])
    reindeers.append(r)


for i in range(1,2504):
    for r in reindeers:
        interval = r.time + r.rest
        if (i % interval) in range(1,r.time+1): # pohybuje se
            r.distance += r.speed
    reindeers.sort(key=lambda x: x.distance, reverse=True)
    max = reindeers[0].distance
    for r in reindeers:
        if r.distance == max: r.points += 1


print("Sorted by distance")
reindeers.sort(key=lambda x: x.points, reverse=True)
for r in reindeers:
    r.print()

print()

print("Sorted by points")
reindeers.sort(key=lambda x: x.points, reverse=True)
for r in reindeers:
    r.print()
