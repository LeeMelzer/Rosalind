sequence = input()
subsequence = input()
count = 0
index = 0

while index < len(sequence):
    nextOccurrence = sequence.find(subsequence, index)

    if (nextOccurrence != -1):
        index = nextOccurrence+1
        count += 1
    else:
        break

print(count)