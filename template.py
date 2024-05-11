import heapq

with open("data.txt") as f:
    lines = f.read().splitlines()

values = list(map(int, lines[1].split()))
heap = []

for value in values:
    heapq.heappush(heap, -value)

print(heap)