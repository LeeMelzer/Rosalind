from collections import defaultdict

with open("data.txt") as f:
    nodes = list(map(int, f.readline().split()))[0]
    edges = [map(int, line.split()) for line in f]

dict = defaultdict(list)
for node, neighbor in edges:
    dict[node].append(neighbor) 

remaining = set(range(2, nodes+1))
result = [0] + [-1]*(nodes-1)
queue = [1]
currentStep = 1

while queue:
    current = queue.pop(0)
    for num in dict[current]:
        if num in remaining:
            queue.append(num)
            remaining.discard(num)
            result[num-1] = result[current-1] + 1

for i, num in enumerate(result):
    if num == nodes+1:
        result[i] = -1

print(*result) 