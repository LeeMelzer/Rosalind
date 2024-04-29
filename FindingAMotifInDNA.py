sequence = input()
substring = input()

def alignStrings(sequenceSlice):
    count = 0
    for i in range(len(substring)):
        if sequenceSlice[i] == substring[i]:
            count += 1

    if count == len(substring):
        return True
    else:
        return False

substringLength = len(substring)
stopIndex = len(sequence) - substringLength
positions = []
for i in range(stopIndex):
    if sequence[i] == substring[0]:
        aligned = alignStrings(sequence[i:i+substringLength])
        if aligned:
            positions.append(i+1)

convertedPositions = map(str, positions)
print(' '.join(convertedPositions))