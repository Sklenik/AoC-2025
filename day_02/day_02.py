with open("./day_02/input.txt",'r') as f:
    inpt = f.read().split(',')

def findRepeatingPattern(item: str)->str:
    strlen = len(item)
    if strlen == 1:
        return ''
    
    if strlen %2 != 0:
        return ''

    for i in range(1,(strlen//2)+1):
        substr = item[0:i]
        if item == substr + substr:
            return substr
    
    return ''

def findRepeatingPatternv2(item: str)->str:
    strlen = len(item)
    if strlen == 1:
        return ''

    patternfound = False
    for i in range(1,strlen+1):
        slicedItem = item
        substr = item[0:i]
        slicedItem = item
        while True:
            if not slicedItem.startswith(substr):
                break
            slicedItem = slicedItem[len(substr):]
            if slicedItem == substr:
                patternfound = True
                break
        if patternfound:
            return substr
    return ''

def main():
    totalpart1 = 0
    totalpart2 = 0

    for rang in inpt:
        rangList = rang.split('-')
        for i in range(int(rangList[0]),int(rangList[1])+1):
            if findRepeatingPattern(str(i)) != '':
                totalpart1 += i
            if findRepeatingPatternv2(str(i)) != '':
                totalpart2 += i

    print(f'Part 1: {totalpart1}')
    print(f'Part 2: {totalpart2}')

main()