with open("data.txt") as f:
    lines = len(f.readlines())

fin = open("data.txt", "r")
fout = open("output.txt", "a")

for i in range(1, lines+1):
    line = fin.readline()
    if (i%2==0):
        fout.write(line)
        
fin.close()
fout.close()
