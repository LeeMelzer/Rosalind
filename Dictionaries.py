string = input()
dict = {}

for word in string.split(' '):
    count = dict.get(word, 0)
    dict[word] = count+1

for key, value in dict.items():
    print(f"{key} {value}")
