def heapify(heap, i):
    if i == 0:
        return
    parent = (i-1)//2
    child = i
    if heap[parent] > heap[child]:
        return
    else:
        heap[parent], heap[child] = heap[child], heap[parent]
        heapify(heap, parent)

def main():
    with open("data.txt") as f:
        n = list(map(int, f.readline().split()))[0]
        arr = list(map(int, f.readline().split()))
    
    heap = []

    for i in range(n):
        heap.append(arr[i])
        heapify(heap, i)

    print(*heap)

if __name__ == "__main__":
    main()