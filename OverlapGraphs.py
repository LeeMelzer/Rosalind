from collections import defaultdict

with open("data.txt") as f:
    lines = f.read().splitlines()

suff = defaultdict(list)
pref = defaultdict(list)
for i in range(0, len(lines), 2):
    stringName = lines[i][1:]
    prefix = lines[i+1][:3]
    suffix = lines[i+1][-3:]
    pref[prefix].append(stringName)
    suff[suffix].append(stringName)

for key, value in suff.items():
    tails = pref.get(key)
    heads = value
    if tails:
        for head in heads:
            for tail in tails:
                if head != tail:
                    print(head, tail)