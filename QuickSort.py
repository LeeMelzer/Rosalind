with open("data.txt") as f:
    n = int(f.readline())
    arr = [int(i) for i in f.readline().split()]

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[j], arr[i]) = (arr[i], arr[j])
    
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

quickSort(arr, 0, n-1)
print(*arr)  