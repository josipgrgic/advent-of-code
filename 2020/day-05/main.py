import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-05//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-05//input.txt') as f:
    lines = [line.rstrip() for line in f]

max_seat_id = 0

encoded_values = {'F' : 0, 'B' : 1, 'R' : 1, 'L' : 0 }

seat_ids = []

def get_decoded_value(encoded):
    value = 0

    for i in range(0, len(encoded)):
        bit_value = encoded_values[encoded[i]]
        power = len(encoded) - 1 - i
        value += bit_value * pow(2, power)
    
    return value


for line in lines:
    m = re.search(r"([FB]{7})([RL]{3})", line)

    (row_str, col_str) = m.groups()

    row = get_decoded_value(row_str)
    col = get_decoded_value(col_str)

    seat_id = row * 8 + col

    print('{}-{} -> {} * 8 + {} = {}'.format(row_str, col_str, row, col, seat_id))

    seat_ids.append(seat_id)

    if (seat_id > max_seat_id):
        max_seat_id = seat_id


print(max_seat_id)

seat_ids.sort()

for i in range(1, len(seat_ids)-1):
    if (seat_ids[i + 1] - seat_ids[i] != 1):
        print(seat_ids[i])
        print('My seat: {}'.format(seat_ids[i] + 1))
        print(seat_ids[i + 1])
        break

