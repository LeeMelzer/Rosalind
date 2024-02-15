str = input()
A, T, C, G = 0, 0, 0, 0

for i in range(len(str)):
    ch = str[i]
    if (ch == 'A'):
        A += 1
    elif (ch == 'T'):
        T += 1
    elif (ch == 'C'):
        C += 1
    else:
        G += 1

print (f"{A} {C} {G} {T}")
