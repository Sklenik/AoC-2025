with open("./day_01/input.txt",'r') as f:
    lines = f.read().splitlines()

def part1():
    pos = 50
    zeroes = 0

    for line in lines:
        sign = 1
        if line[0] == 'L':
            sign = -1
        pos += sign * int(line[1::])
        while pos > 99:
            pos -= 100
        while pos < -99:
            pos += 100
        if pos == 0:
            zeroes += 1
    
    print(f'Part 1: {zeroes}')

def part2():
    pos = 50
    zeroes = 0

    for line in lines:
        sign = 1
        step = 1
        
        if line[0] == 'L':
            sign = -1
            step = -1
        
        startpos = pos
        pos += sign * int(line[1::])
        
        while pos > 99:
            pos -= 100
            zeroes += 1
        
        while pos < -99:
            pos += 100
            zeroes += 1
        
        if startpos == 0:
            startpos += step
        endpos = pos
        if endpos == 0:
            endpos += step

        if 0 in range(startpos, endpos, step):
            zeroes +=1
    
    print(f'Part 2: {zeroes}')
        
part1()
part2()

f.close();