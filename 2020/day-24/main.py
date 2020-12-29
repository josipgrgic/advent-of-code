
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-24//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-24//input.txt') as f:
    lines = [line.rstrip() for line in f]

tiles = []

for line in lines:
    arr = []
    i = 0
    str = ''
    while i < len(line):
        if line[i] in ['s', 'n']:
            arr.append(line[i] + line[i+1])
            i += 2
            continue
        arr.append(line[i])
        i += 1

    tiles.append(arr)

flipped_tiles = {}

def get_adjacent_tiles(x,y):
    return [(x+1,y+1), (x+2,y), (x+1,y-1), (x-1,y-1), (x-2,y), (x-1,y+1)]

def is_tile_black(x,y):
    if (x,y) not in flipped_tiles:
        return False

    return flipped_tiles[(x,y)]

def part_one():
    for tile in tiles:
        x = 0
        y = 0
        for step in tile:
            if step == 'e':
                x += 2
                continue
            elif step == 'se':
                y -= 1
                x += 1
                continue
            elif step == 'sw':
                y -= 1
                x -= 1
                continue
            elif step == 'w':
                x -= 2
                continue
            elif step == 'nw':
                y += 1
                x -= 1
                continue
            elif step == 'ne':
                y += 1
                x += 1
                continue

        if (x,y) not in flipped_tiles:
            flipped_tiles[(x,y)] = True
        else:
            flipped_tiles[(x,y)] = not flipped_tiles[(x,y)]

    count = 0
    for value in list(flipped_tiles.values()):
        if value:
            count += 1

    print('Day {}: {}'.format(0, count))

    for i in range(0,100):
        tiles_to_check = set()
        new_flipped = []

        for (x,y) in list(flipped_tiles.keys()):
            tiles_to_check.add((x,y))
            adjacent_tiles = get_adjacent_tiles(x,y)
            for tile in adjacent_tiles:
                tiles_to_check.add(tile)

        for (x,y) in tiles_to_check:
            adjacent_tiles = get_adjacent_tiles(x,y)
            black_tiles_count = 0

            for at in adjacent_tiles:
                if is_tile_black(at[0], at[1]):
                    black_tiles_count += 1

            if is_tile_black(x,y):
                if black_tiles_count == 0 or black_tiles_count > 2:
                    new_flipped.append((x,y))
                    continue
            else:
                if black_tiles_count == 2:
                    new_flipped.append((x,y))
                    continue

        for flipped in new_flipped:
            if flipped not in flipped_tiles:
                flipped_tiles[flipped] = True
            else:
                flipped_tiles[flipped] = not flipped_tiles[flipped]

        count = 0
        for value in list(flipped_tiles.values()):
            if value:
                count += 1

        print('Day {}: {}'.format(i + 1, count))
                
part_one()

def part_two():
    pass


