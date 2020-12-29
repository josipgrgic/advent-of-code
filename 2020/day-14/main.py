import re
import functools 

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-14//example2.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-14//input.txt') as f:
    lines = [line.rstrip() for line in f]


def parse_command(line):
    [memory_location, value] = re.match(r"mem\[(.*)\] = (.*)", line).groups()
    return (int(memory_location), int(value))

def to_36_bit_binary_string(value):
    result = ''

    for i in range (36, 0, -1):
        if (value >= pow(2, i - 1)):
            value -= pow(2, i - 1)
            result += '1'
        else:
            result += '0'

    return result

def binary_to_decimal(value):
    result = 0

    for i in range(0, len(value)):
        if (value[i] == '0'):
            continue

        result += pow(2, len(value) - 1 - i)

    return result

def part_one():
    mask = ''
    memory = dict()

    for i in range (0, len(lines)):
        m = re.match(r"mask = (.*)", lines[i])

        if (m is not None):
            mask = m.groups()[0]
            continue

        (memory_location, value) = parse_command(lines[i])

        value_binary = to_36_bit_binary_string(value)
        binary_string = ''

        for j in range(0, len(mask)):
            if (mask[j] != 'X'):
                binary_string += mask[j]
            else:
                binary_string += value_binary[j]
        
        result = binary_to_decimal(binary_string)
        memory[memory_location] = result

    result = sum(memory.values())
    print(result)

def part_two():
    mask = ''
    memory = dict()

    for i in range (0, len(lines)):
        m = re.match(r"mask = (.*)", lines[i])

        if (m is not None):
            mask = m.groups()[0]
            continue

        (memory_location, value) = parse_command(lines[i])

        memory_location_binary = to_36_bit_binary_string(memory_location)
        memory_address = ''

        for j in range(0, len(mask)):
            if (mask[j] == 'X' or mask[j] == '1'):
                memory_address += mask[j]
            else:
                memory_address += memory_location_binary[j]
        

        decoded_memory_addresses = ['']

        for j in range(0, len(memory_address)):
            if (memory_address[j] != 'X'):
                for k in range(0, len(decoded_memory_addresses)):
                    decoded_memory_addresses[k] += memory_address[j]

                continue

            zeroes = decoded_memory_addresses[:]
            ones = decoded_memory_addresses[:]

            for k in range(0, len(decoded_memory_addresses)):
                    zeroes[k] += '0'
                    ones[k] += '1'

            decoded_memory_addresses = zeroes + ones


        for mem in decoded_memory_addresses:
            memory[mem] = value
        

    result = sum(memory.values())
    print(result)

part_two()

