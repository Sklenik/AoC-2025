with open("./day_03/input.txt",'r') as f:
    lines = f.read().splitlines()

def findMaxLineJoltage(item: str)->int:
    joltage = ''
    maxJoltage = str(max(item))
    if (item.count(maxJoltage) == 1) and item.endswith(maxJoltage):
        joltage = str(max(item[:item.find(maxJoltage)])) + maxJoltage
    else:
        joltage = maxJoltage + str(max(item[item.find(maxJoltage)+1:]))
    return(int(joltage))
    

def part1():
    totalJoltage = 0
    for line in lines:
        totalJoltage += findMaxLineJoltage(line)
    print(f'Part 1: {totalJoltage}')

part1()

f.close();