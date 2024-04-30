strings = []

with open("data.txt") as f:
    stringList = f.read().splitlines()

currentString = ""
for line in stringList:
    if line[0] == ">" and not currentString:
        continue
    elif line[0] == ">" and currentString:
        strings.append(currentString)
        currentString = ""
    else:
        currentString += line

strings.append(currentString)

profile = [[0 for i in range(len(strings[0]))] for j in range(4)]
for i in range(len(strings)):
    for j in range(len(strings[0])):
        char = strings[i][j]
        if  char == 'A':
            profile[0][j] += 1
        elif char == 'C':
            profile[1][j] += 1
        elif char == 'G':
            profile[2][j] += 1
        else:
            profile[3][j] += 1

consensusString = []
maxValue = [0, 'A']
for i in range(len(profile[0])):
    for j in range(4):
        if profile[j][i] > maxValue[0]:
            maxValue[0] = profile[j][i]
            if j == 0:
                maxValue[1] = 'A'
            elif j == 1:
                maxValue[1] = 'C'
            elif j == 2:
                maxValue[1] = 'G'
            else:
                maxValue[1] = 'T'
    consensusString.append(maxValue[1])
    maxValue[0] = 0
    maxValue[1] = 'A'


print(''.join(consensusString))
print("A:", ' '.join((map(str, profile[0])))) 
print("C:", ' '.join((map(str, profile[1])))) 
print("G:", ' '.join((map(str, profile[2])))) 
print("T:", ' '.join((map(str, profile[3])))) 