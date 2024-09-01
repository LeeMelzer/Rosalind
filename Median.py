import heapq

with open("data.txt") as f:
    n = int(f.readline())
    arr = [int(i) for i in f.readline().split()]
    k = int(f.readline())

heapq.heapify(arr)

for i in range(k-1):
    heapq.heappop(arr)

print(heapq.heappop(arr)) 