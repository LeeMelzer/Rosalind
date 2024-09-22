import heapq

def main():
    with open("data.txt") as f:
        n = int(f.readline().split()[0])
        arr = list(map(lambda x: int(x) * -1, f.readline().split()))
    
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr)*-1)
    
    print(*result)
    

if __name__ == "__main__":
    main()