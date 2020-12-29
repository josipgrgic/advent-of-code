import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-20//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-20//input.txt') as f:
    lines = [line.rstrip() for line in f]

lines.append('eof')

def calculate_hash(array):
    result = 0
    for i in range(0, len(array)):
        if (array[i] == '.'):
            continue

        result += pow(2, len(array) - i - 1)

    return result

class ImageTile(object):

    def calculate_hashes(self):
        self.up_hash = calculate_hash(self.up)
        self.right_hash = calculate_hash(self.right)
        self.down_hash = calculate_hash(self.down)
        self.left_hash = calculate_hash(self.left)

    def process_image(self, image):
        self.image = image

        left_arr = []
        right_arr = []

        for i in range(0, len(image)):
            left_arr.append(image[i][0])
            right_arr.append(image[i][len(image[i])-1])

        self.up = image[0]
        self.right = right_arr
        self.down = image[len(image)-1]
        self.left = left_arr

        self.calculate_hashes()

    def __init__(self, id, image) -> None:
        self.id = id
        self.process_image(image)

        self.tile_up = None
        self.tile_right = None
        self.tile_down = None
        self.tile_left = None
        
    
    def flip_horizontally(self):
        self.image.reverse()
        self.process_image(self.image)

    def flip_vertically(self):
        image = []
        for row in self.image:
            new_row = row[:]
            new_row.reverse()
            image.append(new_row)

        self.process_image(image)

    def rotate(self):
        image = []

        for i in range(0, len(self.image)):
            arr = []
            for j in range(0, len(self.image[i])):
                arr.append(self.image[len(self.image[i]) - 1 - j][i])
            
            image.append(arr)

        self.process_image(image)

def match_tiles_inner2(tile, processed):
    global tiles_dict
    
    if (processed.up_hash == tile.down_hash):
        processed.tile_up = tile
        tile.tile_down = processed

        processed_coord = tiles_dict[processed.id]
        tiles_dict[tile.id] = (processed_coord[0] - 1, processed_coord[1])

        return True

    if (processed.right_hash == tile.left_hash):
        processed.tile_right = tile
        tile.tile_left = processed

        processed_coord = tiles_dict[processed.id]
        tiles_dict[tile.id] = (processed_coord[0], processed_coord[1] + 1)

        return True

    if (processed.down_hash == tile.up_hash):
        processed.tile_down = tile
        tile.tile_up = processed

        processed_coord = tiles_dict[processed.id]
        tiles_dict[tile.id] = (processed_coord[0] + 1, processed_coord[1])

        return True

    if (processed.left_hash == tile.right_hash):
        processed.tile_left = tile
        tile.tile_right = processed

        processed_coord = tiles_dict[processed.id]
        tiles_dict[tile.id] = (processed_coord[0], processed_coord[1] - 1)

        return True

    return False

def match_tiles_inner1(tile, processed):
    for i in range(0,4):
        tile.rotate()
        if (match_tiles_inner2(tile, processed)):
            return True

    return False

def match_tiles(tile, processed):
    if (match_tiles_inner1(tile, processed)):
        return True

    tile.flip_horizontally()

    if (match_tiles_inner1(tile, processed)):
        return True

    tile.flip_horizontally()
    tile.flip_vertically()

    if (match_tiles_inner1(tile, processed)):
        return True

    return False

def is_monsters_head(tile, x, y):
    if y - 17 < 0 or y + 1 > len(tile.image[x]):
        return False
    if x + 2 > len(tile.image):
        return False

    second_row = ''.join(tile.image[x+1][y-18:y+2])
    if re.match(r"#....##....##....###", second_row) is None:
        return False

    second_row = ''.join(tile.image[x+2][y-18:y+2])
    if re.match(r".#..#..#..#..#..#...", second_row) is None:
        return False

    return True

def find_monster_inner2(tile):
    result = 0

    for i in range(0, len(tile.image)):
        for j in range(0, len(tile.image[i])):
            if (tile.image[i][j] == '#'):
                if (is_monsters_head(tile, i,j)):
                    result += 1

    return result

def find_monster_inner1(tile):
    for i in range(0,4):
        tile.rotate()

        result = find_monster_inner2(tile)
        if (result > 0):
            return result
    return 0

def find_monsters(tile):
    result = find_monster_inner1(tile)
    if (result > 0):
        return result

    tile.flip_horizontally()

    result = find_monster_inner1(tile)
    if (result > 0):
        return result

    tile.flip_horizontally()
    tile.flip_vertically()

    result = find_monster_inner1(tile)
    if (result > 0):
        return result

    return 0

tiles = []

current_arr = []
current_id = 0

tiles_dict = {}
tiles_by_id = {}

for line in lines:
    if line == '' or line ==  'eof':
        tile = ImageTile(current_id, current_arr)
        tiles.append(tile)
        tiles_by_id[tile.id] = tile
        current_arr = []
        current_id = 0
        continue
    
    match = re.match(r"Tile (.*):", line)

    if match is not None:
        current_id = int(match.groups()[0])
        continue

    arr = list(line)
    current_arr.append(arr)

def part_one():
    processed = [tiles.pop()]

    tiles_dict[processed[0].id] = (0,0)
    while len(tiles) > 0:
        i = 0
        while i < len(tiles):
            tile = tiles[i]
            matched = False
            j = 0
            while j < len(processed):
                processed_tile = processed[j]
                if (match_tiles(tile, processed_tile)):
                    matched = True
                    break
                j += 1
            
            if matched:
                tiles.pop(i)
                processed.append(tile)

            i += 1

    up_left = processed[0].id
    up_right = processed[0].id
    down_left = processed[0].id
    down_right = processed[0].id

    for id in list(tiles_dict.keys()):
        c = tiles_dict[id]

        if (c[0] <= tiles_dict[up_left][0] and c[1] <= tiles_dict[up_left][1]):
            up_left = id
        if (c[0] <= tiles_dict[up_right][0] and c[1] >= tiles_dict[up_right][1]):
            up_right = id
        if (c[0] >= tiles_dict[down_left][0] and c[1] <= tiles_dict[down_left][1]):
            down_left = id
        if (c[0] >= tiles_dict[down_right][0] and c[1] >= tiles_dict[down_right][1]):
            down_right = id

    print(tiles_dict)

    print(up_left)
    print(up_right)
    print(down_left)
    print(down_right)

    print(up_left * up_right * down_left * down_right)

    (min_i, min_j) = tiles_dict[up_left]
    (max_i, max_j) = tiles_dict[down_right]

    big_image = []

    for i in range(min_i, max_i + 1):
        rows = []
        for j in range(min_j, max_j + 1):
            tile_id = None
            for id, c in tiles_dict.items():
                if (c[0] == i and c[1] == j):
                    tile_id = id
                    break
            
            tile = tiles_by_id[tile_id]
            processed_image = []

            for k in range(1, len(tile.image)-1):
                processed_image.append(tile.image[k][1:len(tile.image[k])-1])

            for k in range(0, len(processed_image)):
                if (k > len(rows) - 1):
                    rows.append(processed_image[k])
                else:
                    rows[k] += processed_image[k]
        
        big_image += rows

    print(big_image)

    image = ImageTile(1, big_image)


    monsters = find_monsters(image)
    
    hash_count = 0

    for i in range(0, len(image.image)):
        for j in range(0, len(image.image[i])):
            if (image.image[i][j] == '#'):
                hash_count += 1
                    

    print(hash_count - monsters * 15)

part_one()
