with open("rosalind_maj.txt") as f:
    lines = f.read().splitlines()

k, n = map(int, lines[0].split())
arrays = []
for line in lines[1:]:
    array = map(int, line.split())
    arrays.append(array)

def findMaximum(array):
    global n
    map = {}
    for num in array:
        map[num] = map.get(num, 0) + 1
        if map.get(num) > n/2:
            return num
    return -1

answers = []
for array in arrays:
    answers.append(findMaximum(array))

print(' '.join(map(str, answers)))  