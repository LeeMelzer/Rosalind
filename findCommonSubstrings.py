import csv

maxCount = 0

# function to align two strings
def alignStrings(string1, string2):
    global maxCount
    maxCount = 0 
    string1Length = len(string1)
    string2Length = len(string2)

    matrix = [[0 for x in range(string1Length)] for y in range(string2Length)]

    for i in range(string2Length):
        for j in range(string1Length):
            if (string2[i] == string1[j]):
                prev = 0
                if (i > 0 and j > 0):
                    prev += matrix[i-1][j-1]
                matrix[i][j] = 1+prev
                maxCount = max(maxCount, matrix[i][j])

    return matrix

# function to iterate over matrix and find counts greater than threshold
def findCommonStrings(matrix, string1):
    global maxCount
    commons = []
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            # setting threshold
            if element == maxCount and maxCount >= 6:
                string = getString(matrix, i, j, string1)
                commons.append(''.join(string))
    
    return commons

# function to get string from matrix and reverse 
def getString(matrix, i, j, string1):
    string = []
    while i >= 0 and j >= 0 and matrix[i][j] >= 1:
        string.append(string1[j])
        i-=1
        j-=1
    
    string.reverse() 
    return string

def main():
    # take the input from text file as list of lists
    with open("data.txt") as f:
        stringList = [line for line in f]

    global maxCount

    commonStrings = {}
    listOfCommons = []

    # for loops to iterate over entire list and compare each string
    for i in range(len(stringList)):
        for j in range(i+1, len(stringList)):
            string1 = stringList[i]
            string2 = stringList[j]
            matrix = alignStrings(string1, string2)
            listOfCommons.append(findCommonStrings(matrix, string1))
    
    # add each string to commonStrings and count
    for string in listOfCommons:
        s = str(string)
        commonStrings[s] = commonStrings.get(s, 0) + 1

    with open("output.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in commonStrings.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    main()