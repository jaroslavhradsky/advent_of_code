# Formula based Python3 code to find  
# sum of all divisors of n. 
# https://www.geeksforgeeks.org/sum-factors-number/
import math as m 
import time

# Returns sum of all factors of n. 
def sumofFactors(n):     
    # Traversing through all prime factors 
    res = 1
    for i in range(2, int(m.sqrt(n) + 1)): 
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            n = n / i
            curr_term = curr_term * i
            curr_sum += curr_term
        res = res * curr_sum 
      
    # This condition is to handle the case when n is a prime number greater than 2 
    if n > 2: 
        res = res * (1 + n) 
    return int(res)
  
# i = 1
# start = time.perf_counter()
# while True:
#     sum = sumofFactors(i)
#     if sum >= 3400000: 
#         print ("House:",i,"Presents:",sumofFactors(i),"Time:",time.perf_counter()-start)

elves = dict()
house = 1
while True:
    elves[house] = 50
    presents = 0
    for key in elves.keys():
        elve = elves.get(key)
        if elve > 0 and house % key == 0:
            elves[key] = elve - 1
            presents += elve * 11
    #print(elves)
    if presents > 34000000 or house % 10000 == 0:
        print("House:",house,"Presents:",presents)
        print(elves)
    house += 1

