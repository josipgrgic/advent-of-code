import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-09//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-09//input.txt') as f:
    numbers = [int(line.rstrip()) for line in f]

def get_permutations(current_index, preamble_length):
    list = []
    for i in range(current_index - preamble_length, current_index):
        for j in range(i + 1, current_index):
            list.append((numbers[i], numbers[j]))

    return list

def part_one():
    preamble_length = 25
    current_index = preamble_length

    invalid_number_index = -1
    while invalid_number_index == -1 or current_index < len(numbers):
        current_number= numbers[current_index]
        print('Current number: {}'.format(current_number))

        preamble = get_permutations(current_index, preamble_length)

        print(preamble)

        is_valid = False

        for (first, second) in preamble:
            if (first + second == current_number):
                is_valid = True
                break

        if (not is_valid):
            invalid_number_index = current_index
            break

        current_index += 1

    print('First invalid number: {}'.format(numbers[invalid_number_index]))

#invalid_number = 127
invalid_number = 375054920

def part_two():
    start_index = 0
    end_index = 2

    smallest = float('inf')
    biggest = 0

    result = -1

    while result == -1 or end_index > len(numbers):
        sum = 0
        smallest = float('inf')
        biggest = 0

        for i in range(start_index, end_index):
            number = numbers[i]

            sum += number

            if (sum > invalid_number):
                break

            if (number > biggest):
                biggest = number

            if (number < smallest):
                smallest = number

        if (sum == invalid_number):
            result = smallest + biggest
        elif (sum > invalid_number):
            start_index += 1
            end_index = start_index + 2
        else:
            end_index += 1

    print('Found a set from index {} to index {}'.format(start_index, end_index))
    print('Smallest: {}; Biggest {}'.format(smallest, biggest))
    print(result)

part_two()


