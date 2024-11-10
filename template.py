import heapq

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             (arr[j], arr[i]) = (arr[i], arr[j])
    
#     (arr[i+1], arr[high]) = (arr[high], arr[i+1])
#     return i+1

# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, 0, pi-1)
#         quickSort(arr, pi+1, high)

def main():
    # quickSort(arr, 0, len(arr)-1)
    arr = [1, 3, 6, 9, 69, -7]
    heapq.heapify(arr)
    result = []

    while arr:
        result.append(heapq.heappop(arr))

    print(*result)

if __name__ == "__main__":
    main()