with open("data.txt") as f:
    lines = f.read().splitlines()

n = int(lines[0])
arr = list(map(int, lines[1].split()))
swaps = 0

def insertionSort(arr, n):
    global swaps
    for i in range(1, n):
        key = arr[i]
        k = i-1
        
        while k >= 0 and key < arr[k]:
            swaps += 1
            arr[k+1] = arr[k]
            k -= 1

        arr[k+1] = key 

insertionSort(arr, n)
print(swaps)