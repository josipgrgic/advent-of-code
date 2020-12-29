import itertools

with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-01//input.txt') as f:
    lines = [line.rstrip() for line in f]

for (x, y, z) in itertools.combinations(lines, r=3):
    first = int(x)
    second = int(y)
    third = int(z)

    if (first + second + third == 2020):
        print('{} + {} + {} = 2020'.format(first, second, third))
        print(first * second * third)
        break

print('end')

def manage_a_trois(first, second, third): 
    if (first + second + third == 2020):
        print('{} + {} + {} = 2020'.format(first, second, third))
        print(first * second * third)
        return True

    return False

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        for k in range(j+1, len(lines)):
            first = int(lines[i])
            second = int(lines[j])
            third = int(lines[k])

            if (manage_a_trois(first, second, third)):
                break

print('end')


