def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    
    if left:
        result += left
    if right:
        result += right
    return result

def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    sLeft = mergeSort(left)
    sRight = mergeSort(right)
    return merge(sLeft, sRight)

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()

    n = lines[0]
    string = ""
    for line in lines[1:]:
        string += line 

    arr = list(map(int, string.split(" ")))
    sorted = mergeSort(arr)
    print(' '.join(map(str, sorted)))

if __name__ == "__main__":
    main()
