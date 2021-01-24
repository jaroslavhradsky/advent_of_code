# --- Day 7: Some Assembly Required ---

# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

#     123 -> x means that the signal 123 is provided to wire x.
#     x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
#     p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
#     NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i

# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

# Your puzzle answer was 46065.
# --- Part Two ---

# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

# Your puzzle answer was 14134.

# &  	AND 	Sets each bit to 1 if both bits are 1
# | 	OR 	Sets each bit to 1 if one of two bits is 1
#  ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
# ~  	NOT 	Inverts all the bits
# << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


def show_wires(w):
    for key, val in w.items():
        print(key, type(val), (val))

def logic(lst):
    if len(lst) == 1:
        return(lst[0])
    if len(lst) == 2:
        return 65535 - lst[1]
    else:
        if lst[1] == "AND": 
            #print(lst)
            return lst[0] & lst[2]
        if lst[1] == "OR": return lst[0] | lst[2]
        if lst[1] == "RSHIFT": return lst[0] >> lst[2]
        if lst[1] == "LSHIFT": return lst[0] << lst[2]
    return lst

def all_solved(w):
    w = dict(w)
    for val in w.values():
        if type(val) != "<class 'int'>": return False
    return True 

# load input
wires = dict()
for line in open("day07-input2.txt"):   
    key = line.split(" -> ")[1].strip()
    val = line.split(" -> ")[0].split() 
    if len(val) == 1 and str(val[0]).isnumeric(): val = int(val[0])
    wires[key] = val 

just_numbers = dict()
while len(wires) > 0:
    # zarad do seznamu hotovych ty co uz jsou jen cislo + vymaz je z puvodniho
    for key, val in wires.items():
        if type(val) == int: 
            just_numbers[key] = int(val)
            
    for key in just_numbers.keys(): 
        if key in wires.keys(): wires.pop(key)

    # nahrad zname promenne hodnotama
    for key in wires.keys():
        val = wires.get(key)
        solve = True
        for i in range(len(val)):
            if val[i] in just_numbers.keys(): val[i] = just_numbers[val[i]]
            if str(val[i]).isnumeric(): val[i] = int(val[i])
            if str(val[i]).islower(): solve = False
        if solve:
            wires[key] = logic(val)

print("Signal on wire 'a' is: ", just_numbers["a"])
