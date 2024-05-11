with open("data.txt") as f:
    lines = f.read().splitlines()

arr = []
for line in lines[1:]:
    arr.append(list(map(int, line.split())))

def find2Sum(array):
    dict = {}
    for i, num in enumerate(array):
        if dict.get(num) or dict.get(num) == 0:
            print(dict.get(num)+1, i+1)
            return
        else:
            dict[-num] = i

    print(-1)


for array in arr:
    find2Sum(array) 