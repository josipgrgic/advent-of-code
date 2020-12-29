#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-03//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-03//input.txt') as f:
    lines = [line.rstrip() for line in f]

tree = "#"
open_square = "."

right_delta = 3
down_delta = 1

current_x = right_delta
current_y = down_delta

class SlopeData:
    def __init__(self, delta_x, delta_y):
        self.delta_x = delta_x
        self.current_x = delta_x
        self.delta_y = delta_y
        self.current_y = delta_y
        self.trees = 0

slope_data = [
    SlopeData(1,1),
    SlopeData(3,1),
    SlopeData(5,1),
    SlopeData(7,1),
    SlopeData(1,2)
]


print("length of tree segment:", len(lines[0]))

for i in range(len(lines)):
    for slope in slope_data:
        if (slope.current_y != i):
            continue

        if (lines[slope.current_y][slope.current_x] == tree):
            slope.trees += 1

        slope.current_y += slope.delta_y
        slope.current_x = (slope.current_x + slope.delta_x) % len(lines[0])

res = 1

for slope in slope_data:
    print(slope.trees)
    res *= slope.trees

print(res)
