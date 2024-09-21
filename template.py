import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1

def setRandomPivot(arr, low, high):
    randPivot = random.randint(low, high)
    (arr[high], arr[randPivot]) = (arr[randPivot], arr[high])
    return partition(arr, low, high)

def quickSort(arr, low, high):
    if low < high:
        pi = setRandomPivot(arr, low, high)
        quickSort(arr, 0, pi-1)
        quickSort(arr, pi+1, high)

def main():
    with open("data.txt") as f:
        n = int(f.readline().split()[0])
        arr = list(map(int, f.readline().split()))

    quickSort(arr, 0, len(arr)-1)
    print(*arr)

if __name__ == "__main__":
    main()