maxGC = 0
maxId = ""
seqId = ""
sequence = ""

def findGC():
    global maxGC, maxId, sequence, seqId
    count = 0
    for base in sequence:
        if base == "C" or base == "G":
            count += 1
    
    content = (count / len(sequence)) * 100
    if content > maxGC:
        maxGC = content
        maxId = seqId

with open("data.txt") as f:
    myList = f.read().splitlines()

for line in myList:
    if line[0] == ">" and sequence:
        findGC()
        seqId = line[1:]
        sequence = ""
        continue
    elif line[0] == ">" and not sequence:
        seqId = line[1:]
        continue
    else:
        sequence += line

findGC()
maxGC = round(maxGC, 6)
print(f"{maxId}\n{maxGC}") 