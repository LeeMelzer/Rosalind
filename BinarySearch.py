with open("rosalind_bins.txt") as f:
    lines = f.read().splitlines()

n = int(lines[0])
k = int(lines[1])
sortedArray = list(map(int, lines[2].split()))
keys = list(map(int, lines[3].split()))

def binarySearch(key, left, right):
    if right >= left:
        mid = (right + left) // 2
        if sortedArray[mid] == key:
            return mid+1
        elif key < sortedArray[mid]:
            return binarySearch(key, left, mid-1)
        else:
            return binarySearch(key, mid+1, right) 
    else:
        return -1

answers = []
for num in keys:
    answers.append(binarySearch(num, 0, n))

print(' '.join(map(str, answers))) 