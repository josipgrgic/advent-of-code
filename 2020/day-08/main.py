import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-08//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-08//input.txt') as f:
    lines = [line.rstrip() for line in f]

acc = 'acc'
jmp = 'jmp'
nop = 'nop'

accumulator = 0
program_terminated_correctly = False
switched_operation_index = -1

while not program_terminated_correctly:

    i = switched_operation_index + 1

    while i < len(lines):
        [operation, argument_str] = lines[i].split(' ')
        if (operation == jmp or operation == nop):
            switched_operation_index = i
            print('Changing {} operation at line {}'.format(operation, i + 1))
            break
        i += 1

    visited_lines = set()
    current_line_number = 0
    accumulator = 0

    print('New run, changed line: {}'.format(i + 1))

    while True:
        if (current_line_number == len(lines)):
            program_terminated_correctly = True
            break

        if (current_line_number in visited_lines):
            break

        visited_lines.add(current_line_number)

        print(lines[current_line_number])

        [operation, argument_str] = lines[current_line_number].split(' ')

        if (current_line_number == switched_operation_index):
            if (operation == jmp):
                operation = nop
            else:
                operation = jmp

        argument = int(argument_str)

        if (operation == acc):
            accumulator += argument
            current_line_number += 1
        elif (operation == jmp):
            current_line_number += argument
        elif (operation == nop):
            current_line_number += 1

print(accumulator)