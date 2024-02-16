n = int(input())
oneGenBack = 1
twoGenBack = 1

for i in range(2, n):
    temp = oneGenBack + twoGenBack
    twoGenBack = oneGenBack
    oneGenBack = temp

print (oneGenBack)
