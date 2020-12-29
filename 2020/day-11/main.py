
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-11//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-11//input.txt') as f:
    lines = [line.rstrip() for line in f]

floor = '.'
empty = 'L'
occupied = '#'

seating = []

for line in lines:
    seating.append(list(line))

def copy_seating():
    copy = []
    for row in seating:
        copy.append(row[:])
    return copy

def count_adjacent_occupied(row, col, seating):
    count = 0
    
    adjacent_points = [
        (row-1,col-1), (row-1,col), (row-1,col+1),
        (row,col-1)  ,              (row,col+1),
        (row+1,col-1), (row+1,col), (row+1,col+1),
    ]

    for (i,j) in adjacent_points:
        if (i < 0 or i > len(seating)-1):
            continue
        if (j < 0 or j > len(seating[0])-1):
            continue

        if (seating[i][j] == occupied):
            count += 1

    return count 

def count_adjacent_occupied_2(row, col, seating):
    count = 0
    
    pointers = [
        [row, col, 0, -1, False],   # Left
        [row, col, 0, 1, False],    # Right
        [row, col, -1, 0, False],   # Up
        [row, col, 1, 0, False],    # Down
        [row, col, -1, 1, False],   # Up Right
        [row, col, -1, -1, False],  # Up Left
        [row, col, 1, 1, False],    # Down Right
        [row, col, 1, -1, False]    # Down Left
    ]

    pointers_resolved = False

    while not pointers_resolved:
        pointers_resolved = True
        
        for pointer in pointers:
            # Check if already resolved
            if (pointer[4]):
                continue

            # make step
            pointer[0] += pointer[2]
            pointer[1] += pointer[3]

            # check if out of bounds
            if (pointer[0] < 0 or pointer[0] > len(seating)-1):
                pointer[4] = True
                continue

            if (pointer[1] < 0 or pointer[1] > len(seating[0])-1):
                pointer[4] = True
                continue

            # check if seat
            if (seating[pointer[0]][pointer[1]] != floor):
                pointer[4] = True
                if (seating[pointer[0]][pointer[1]] == occupied):
                    count += 1
                continue

            pointers_resolved = False

    return count 


def part_one():
    had_changes = True
    while had_changes:
        had_changes = False
        seating_copy = copy_seating()

        for i in range(0, len(seating)):
            for j in range(0,len(seating[i])):
                if (seating[i][j] == floor):
                    continue

                count = count_adjacent_occupied_2(i, j, seating_copy)

                current_seat = seating[i][j]

                if (current_seat == empty and count == 0):
                    seating[i][j] = occupied
                    had_changes = True
                    continue
                if (current_seat == occupied and count >= 5):
                    had_changes = True
                    seating[i][j] = empty

        print('\n'.join([''.join([str(cell) for cell in row]) for row in seating]))
        print()

    occupied_count_final = 0

    for i in range(0, len(seating)):
        for j in range(0,len(seating[i])):
            if (seating[i][j] == occupied):
                occupied_count_final += 1

    print(occupied_count_final)
    

part_one()

def part_two():
    pass


