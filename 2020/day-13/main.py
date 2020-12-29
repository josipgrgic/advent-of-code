from functools import reduce

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-13//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-13//input.txt') as f:
    [timestamp, bus_ids] = [line.rstrip() for line in f]

time = int(timestamp)
bus_arr = bus_ids.split(',')

def part_one():
    id = 0,
    minutes = float('inf')
    

    for bus in bus_arr:
        if (bus == 'x'):
            continue

        bus_id = int(bus)
        mod = time % bus_id

        if (mod == 0):
            minutes = 0
            id = bus_id
            break

        val = int(time/bus_id) * bus_id + bus_id

        diff = bus_id - mod

        if (diff < minutes):
            minutes = diff
            id = bus_id

    print('{} * {} = {}'.format(id, minutes, id * minutes))

def validate(ts):
    for i in range(0, len(bus_arr)):
        if (bus_arr[i] == 'x'):
            continue

        id = int(bus_arr[i])

        if ((ts+i) % id != 0):
            return False

    return True

def part_two():
    first_id = int(bus_arr[0])
    last_id = int(bus_arr[-1])

    ts = first_id
    t = 0

    while True:
        t += 1

        if (t % 1000000 == 0):
            print(t)

        ts += first_id

        if ((ts + len(bus_arr) - 1) % last_id == 0):
            is_valid = validate(ts)
            if (is_valid):
                break

    print(t * first_id)

def gcdExtended(a, b):
    if a == 0 :   
        return b, 0, 1
             
    gcd, x1, y1 = gcdExtended(b%a, a)  
     
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd, x, y 

def chinese(arr):
    ids = []
    offsets = []
    N = 1

    for i in range(0, len(arr)):
        if (arr[i] == 'x'):
            continue

        id = int(arr[i])

        ids.append(id)
        if (i == 0):
            offsets.append(i)
        else:
            offsets.append(id - i)

        N *= id

    x = 0

    for i in range(0, len(ids)):
        ni = ids[i]

        N_div_ni = int(N / ni)

        (gcd, r, s) = gcdExtended(ni, N_div_ni)

        x += offsets[i] * s * N_div_ni

    print(x % N)

chinese(bus_arr)

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-13//e2.txt') as f:
#   lines = [line.rstrip() for line in f]

#for line in lines:
#    arr = line.split(',')
#    chinese(arr)