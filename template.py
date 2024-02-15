str = input()
strout = ""

for i in range(len(str)-1, -1, -1):
    ch = str[i]
    if (ch == 'A'):
        strout += 'T'
    elif (ch == 'T'):
        strout += 'A'
    elif (ch == 'C'):
        strout += 'G'
    else:
        strout += 'C'

print(strout)
