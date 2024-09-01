with open("data.txt") as f:
    n = int(f.readline().strip())
    arr = [int(i) for i in f.readline().strip().split(" ")]

pivot = arr[0] 
mid = []
mid.append(pivot)
left = []
right = []
for i in range(1, len(arr)):
    num = arr[i] 
    if num < pivot:
        left.append(num)
    elif num == pivot:
        mid.append(num)
    else:
        right.append(num)

result = left + mid + right

print(*result) 