n, k = map(int, input().split())

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

nFactorial = factorial(n)
nMinusKFactorial = factorial(n-k)

result = (nFactorial / nMinusKFactorial) % 1000000
print(int(result))