import heapq
    
def main():
    arr = [1, 5, 9, 0, 23, -8]

    heapq.heapify(arr)
    result = []

    while arr:
        result.append(heapq.heappop(arr))
    
    print(*result)

if __name__ == "__main__":
    main() 