import re
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-12//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-12//input.txt') as f:
    lines = [line.rstrip() for line in f]

directions = ['E', 'S', 'W', 'N']

def part_one():
    x = 0
    y = 0
    direction = 0

    for line in lines:
        print('({},{})-{}'.format(x,y,directions[direction]))
        print(line)

        (action, value_str) = re.match(r"(.)(.*)", line).groups()

        value = int(value_str)

        if (action == 'F'):
            action = directions[direction]

        if (action == 'N'):
            y += value
        elif (action == 'S'):
            y -= value
        elif (action == 'E'):
            x += value
        elif (action == 'W'):
            x -= value
        elif (action == 'L'):
            rotation = int(value / 90)
            direction = (direction - rotation) % len(directions)
        elif (action == 'R'):
            rotation = int(value / 90)
            direction = (direction + rotation) % len(directions)
        else:
            print('WTF')

        print('({},{})-{}'.format(x,y,directions[direction]))
        print()

    print(abs(x)+abs(y))

qs = [(1,1), (1,-1), (-1,-1), (-1,1)]

def get_q(wx, wy):
    qx = 0
    qy = 0

    if (wx != 0):
        qx = int(wx / abs(wx))

    if (wy != 0):
        qy = int(wy / abs(wy))

    for i in range(0,len(qs)):
        if ((qx == qs[i][0] or qx == 0) and (qy == qs[i][1] or qy == 0)):
            return i

def part_two():
    x = 0
    y = 0

    wx = 10
    wy = 1

    for line in lines:
        print('({},{})-({},{})'.format(x,y,wx,wy))
        print(line)

        (action, value_str) = re.match(r"(.)(.*)", line).groups()

        value = int(value_str)

        if (action == 'F'):
            x += wx * value
            y += wy * value
        elif (action == 'N'):
            wy += value
        elif (action == 'S'):
            wy -= value
        elif (action == 'E'):
            wx += value
        elif (action == 'W'):
            wx -= value
        elif (action == 'L' or action == 'R'):
            qi = get_q(wx, wy)
            rotation = int(value / 90)

            if (action == 'L'):
                rotation *= -1

            new_qi = (qi + rotation) % len(qs)
            new_wx = wx
            new_wy = wy

            if (rotation % 2 != 0):
                new_wx = wy
                new_wy = wx

            wx = abs(new_wx) * qs[new_qi][0]
            wy = abs(new_wy) * qs[new_qi][1]
        else:
            print('WTF')

        print('({},{})-({},{})'.format(x,y,wx,wy))
        print()

    print(abs(x)+abs(y))


part_two()