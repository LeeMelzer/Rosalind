n, k = map(int, input().split())
oneGenBack = 1
twoGenBack = 1

for i in range(2, n):
    temp = (twoGenBack * k) + oneGenBack
    twoGenBack = oneGenBack
    oneGenBack = temp

print (oneGenBack)
