def twoSum(nums, target, index):
    map = {}
    for i, num in enumerate(nums):
        difference = target + num
        if -difference in map:
            return [map[-difference]+index, i+index]
        else:
            map[num] = i

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    
    n, k = lines[0].split()
    arrays = []
    for line in lines[1:]:
        array = list(map(int, line.split()))
        arrays.append(array)
    
    for array in (arrays):
        for i, num in enumerate(array):
            result = twoSum(array[i+1:], num, i+2)
            if result:
                result.insert(0, i+1)
                break

        if result:
            print(*result)
        else:
            print(-1)

if __name__ == "__main__":
    main()