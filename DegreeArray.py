from collections import defaultdict

with open("data.txt") as f:
    lines = f.read().splitlines()

n, m = map(int, lines[0].split())
graph = defaultdict(list)
for line in lines[1:]:
    node, edge = map(int, line.split())
    graph[node].append(edge)
    graph[edge].append(node)
    
result = [0] * (n+1) 
for key, value in graph.items():
    result[int(key)] = len(value)

result.pop(0)
print(' '.join(map(str, result))) 