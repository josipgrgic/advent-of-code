import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-19//example.txt') as f:
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-19//example2.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-19//input.txt') as f:
    lines = [line.rstrip() for line in f]

rules = {}
i = 0
for i in range(0, len(lines)):
    line = lines[i]

    if (line == ''):
        break

    [index, rule] = re.match(r"(.*): (.*)", line).groups()
    rule_arr = rule.split('|')
    arr = []

    for r in rule_arr:
        a = []
        for x in r.strip().split(' '):
            if (x.isnumeric()):
                a.append(int(x))
            else:
                a.append(re.match(r"\"(.*)\"", x).groups()[0])
        arr.append(a)
    
    rules[int(index)] = arr

def match(line, current):
    j = 0
    for i in range(0, len(line)):
        j = i
        if (i > len(current) - 1):
            return False

        char1 = line[i]
        char2 = current[i]

        if (isinstance(char2, int)):
            for r in rules[char2]:
                new_current = r + current[i + 1:]
                result = match(line[i:], new_current)
                if (result):
                    return True
            
            return False
        
        if (char1 != char2):
            return False

    if (j < len(current) -1):
        return False

    return True

def part_one():
    result = 0
    for j in range(i+1, len(lines)):
        line = lines[j]
        current = rules[0][0]

        does_match = match(line, current)

        if (does_match):
            print(line)
            result += 1

    print(result)

part_one()
