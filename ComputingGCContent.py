largestGCContent = ""
currentStringLabel = ""
sequence = ""

with open("data.txt", "r") as f:
    for line in f:
        if (line.startswith('>')):
            str = line
            currentStringLabel= str[1:]
