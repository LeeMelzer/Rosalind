str = input()
strout = ""

for i in range(len(str)):
    if (str[i] == 'T'):
        strout += 'U'
    else:
        strout += str[i]

print(strout)
