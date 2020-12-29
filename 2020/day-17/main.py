
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-17//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-17//input.txt') as f:
    lines = [line.rstrip() for line in f]

cube_states = {}
active = "#"
inactive = "."

for x in range(0, len(lines)):
    line = lines[x]
    for y in range(0, len(line)):
        cube = line[y]
        cube_states[(x,y,0,0)] = cube

def get_cube_activity(cube):
    global cube_states
    (x,y,z,w) = cube
    if (x,y,z,w) in cube_states:
        return cube_states[(x,y,z,w)]

    return inactive

def count_active_cubes_in_neighborhood(cube):
    (x,y,z,w) = cube
    active_cubes = 0

    for x1 in range(x-1, x+2):
        for y1 in range(y-1, y+2):
            for z1 in range(z-1, z+2):
                for w1 in range(w-1, w+2):
                    activity = get_cube_activity((x1,y1,z1,w1))
                    if (activity == active):
                        active_cubes += 1

    if (get_cube_activity(cube) == active):
        active_cubes -= 1

    return active_cubes

def get_all_potential_cubes_to_change():
    global cube_states

    cubes = set()

    for cube in list(cube_states.keys()):
        for x in range(cube[0]-1, cube[0]+2):
            for y in range(cube[1]-1, cube[1]+2):
                for z in range(cube[2]-1, cube[2]+2):
                    for w in range(cube[3]-1, cube[3]+2):
                        cubes.add((x,y,z,w))

    return cubes
    

def part_one():
    global cube_states
    for i in range(0,6):
        new_cube_states = {}
        cubes = get_all_potential_cubes_to_change()
        for cube in cubes:
            activity = get_cube_activity(cube)
            active_neighbor_cube_count = count_active_cubes_in_neighborhood(cube)
            if (activity == active):
                if ((active_neighbor_cube_count == 2 or active_neighbor_cube_count == 3)):
                    new_cube_states[cube] = active
                else:
                    new_cube_states[cube] = inactive
            else:
                if (active_neighbor_cube_count == 3):
                    new_cube_states[cube] = active
                else:
                    new_cube_states[cube] = inactive
        
        cube_states = new_cube_states

    count = 0
    for activity in list(cube_states.values()):
        if (activity == active):
            count += 1

    print(count)

part_one()

def part_two():
    pass


