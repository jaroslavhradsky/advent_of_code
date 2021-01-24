import re
input = open("day12-input.txt").read()
numbers = re.findall("[-]*[0-9]+", input)
sum = 0
for number in numbers: sum += int(number)
print("Sum of all numbers is: ", sum)



# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.

lst = list()
for i in range(0, len(input)):
    ch = input[i]
    if ch in "{[": lst.append(ch)
    elif ch in "}]":
        lst.pop()
    else:
        pass

