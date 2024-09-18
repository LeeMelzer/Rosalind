import heapq

with open("data.txt") as f:
    n = list(map(int, f.readline().split()))[0]
    arr = list(map(int, f.readline().split()))

result = []
heapq.heapify(result)
while arr:
    result.append(heapq.heappop(arr))

print(*result) 