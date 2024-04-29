seq1 = input()
seq2 = input()
hamming = 0

for i in range (len(seq1)):
    if seq1[i] != seq2[i]:
        hamming += 1

print(hamming)  