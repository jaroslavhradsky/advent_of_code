import re
def sector_id(name):
    room = re.findall(r"(.*)-[0-9]*\[", name)[0]
    id = re.findall(r".*-([0-9]*)\[", name)[0]
    hash = re.findall(r"\[(.*)\]", name)[0]
    
    letters = dict()
    for ch in room:
        if ch.isalpha():
            letters[ch] = letters.get(ch, 0) + 1
    print(letters)

    lst = list()
    

print(sector_id("a-b-c-d-eeee-f-g-h-987[abcde]"))