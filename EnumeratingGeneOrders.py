def findFactorial(num):
    if num == 1:
        return 1
    
    return num * findFactorial(num-1)

num = int(input())
print(findFactorial(num))

permutations = []
def backtrack(hashset):
    if len(hashset) == num:
        permutation = list(hashset)
        permutations.append(permutation)
        return

    for i in range(1, num+1):
        if i not in hashset:
            hashset.append(i)
            backtrack(hashset)
            hashset.pop()

hashset = []
backtrack(hashset)

for permutation in permutations:
    print(' '.join(map(str, permutation)))
