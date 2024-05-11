with open("data.txt") as f:
    lines = f.read().splitlines()

n = int(lines[0])
m = int(lines[2])
A = list(map(int, lines[1].split()))
B = list(map(int, lines[3].split()))

merged = []
i, j = 0, 0
while (i < n and j < m):
    if A[i] < B[j]:
        merged.append(A[i])
        i += 1
    else:
        merged.append(B[j])
        j += 1

while (i < n):
    merged.append(A[i])
    i += 1

while (j < m):
    merged.append(B[j])
    j += 1

print(' '.join(map(str, merged))) 