def getInput(inputfile):   
    data = []
    with open(inputfile, 'r') as f:
        for line in f:
            if line != '\n':
                 data.append(eval(line.strip()))
    return data

def sortAndSearch(aData):
    aData.sort()
    i = 0
    j = len(aData) - 1
    while i < j:
        if aData[i] + aData[j] == 2020:
            return aData[i], aData[j]
        elif aData[i] < 2020 - aData[j]:
            i += 1
        else:
            j -= 1


if __name__ == "__main__":
    
    solution = sortAndSearch(getInput('input.txt'))
    
    print(solution)

    
