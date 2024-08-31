from collections import defaultdict

with open("data.txt") as f:
    lines = f.read().splitlines()

length, edges = map(int, lines[0].split())
dict = defaultdict(list)

for i in range(1, length+1):
    string = str(i)
    dict[string] 

for i in range(1, len(lines)):
    n, k = map(str, lines[i].split())
    dict[n].append(k)
    dict[k].append(n)

result = []
for key, value in dict.items():
    sum = 0
    for val in dict.get(key): 
        degree = len(dict.get(val))
        sum += degree
    
    result.append(sum)

print(*result) 