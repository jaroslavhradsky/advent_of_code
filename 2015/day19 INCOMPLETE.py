repl = dict()
molecule = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

for line in open("day19-input.txt"):
    key = line.split(" => ")[0]
    val = line.split(" => ")[1].strip()
    vals = repl.get(key, list())
    vals.append(val)
    repl[key] = vals

molecules = list()
i = 0
while i < len(molecule):
    txt = molecule[i]
    ltext = 1
    if i != len(molecule)-1 and molecule[i+1].islower(): 
        txt += molecule[i+1]
        ltext = 2
    if txt in repl:
        for r in repl[txt]:
            new_molecule = molecule[:i] + r + molecule[i+ltext:]
            if new_molecule not in molecules: molecules.append(new_molecule)
    i += ltext
print("Number of molecules is:",len(molecules))


# to mam strasne pomaly, takze to asi budu muset zkusit udelat slovnik na druhou stranu
# Step 1. Longest molecule: 3. Number of molecules is: 3. Time of calculation: 0.0000
# Step 2. Longest molecule: 11. Number of molecules is: 18. Time of calculation: 0.0000
# Step 3. Longest molecule: 14. Number of molecules is: 105. Time of calculation: 0.0003
# Step 4. Longest molecule: 20. Number of molecules is: 607. Time of calculation: 0.0065
# Step 5. Longest molecule: 23. Number of molecules is: 3566. Time of calculation: 0.2595
# Step 6. Longest molecule: 29. Number of molecules is: 21287. Time of calculation: 16.2788
# Step 7. Longest molecule: 32. Number of molecules is: 129071. Time of calculation: 457.3361


import time

molecules = ["e"]

step = 1

to_find = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"
while to_find not in molecules:
    start = time.perf_counter()
    new_molecules = list()
    for molecule in molecules:
        i = 0
        while i < len(molecule):
            txt = molecule[i]
            ltext = 1
            if i != len(molecule)-1 and molecule[i+1].islower(): 
                txt += molecule[i+1]
                ltext = 2
            if txt in repl:
                for r in repl[txt]:
                    #print(key,repl[key])
                    new_molecule = molecule[:i] + r + molecule[i+ltext:]
                    if new_molecule not in new_molecules: new_molecules.append(new_molecule)
            i += ltext
    
    stop = time.perf_counter()
    longest = 0
    for m in new_molecules:
        if len(m) > longest: longest = len(m)

    print("Step %d. Longest molecule: %d. Number of molecules is: %d. Time of calculation: %0.4f" % (step, longest, len(new_molecules), stop - start))        
    step += 1
    molecules = new_molecules
    #print(molecules)
    #input()
print(step)