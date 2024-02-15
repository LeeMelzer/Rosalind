s = input()
a, b, c, d = map(int, input().split())

first = s[a:b+1]
second = s[c:d+1]

print(f"{first} {second}")
