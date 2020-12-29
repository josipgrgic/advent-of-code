import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-02//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-02//input.txt') as f:
    lines = [line.rstrip() for line in f]

valid_passwords_count = 0

def parse_line(line):
    [policy, password] = line.split(":")
    [bounds, letter] = policy.split()
    [first_index_str, second_index_str] = bounds.split("-")

    first_index = int(first_index_str)
    second_index = int(second_index_str)

    return [first_index, second_index, letter, password.strip()]

def parse_line_2(line):
    m = re.search(r"([0-9]+)-([0-9]+) (\w): (\w+)", line)

    return [int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)]

def is_password_valid_1(lower_bound, upper_bound, letter, password):
    number_of_occurrences = 0

    for char in password:
        if (char != letter):
            continue

        number_of_occurrences += 1

        if (number_of_occurrences > upper_bound):
            # Too many occurrences
            break

    return number_of_occurrences >= lower_bound and number_of_occurrences <= upper_bound

def is_password_valid_2(first_index, second_index, letter, password):
    number_of_occurrences = 0

    if (password[first_index - 1] == letter):
        number_of_occurrences += 1
    
    if (password[second_index - 1] == letter):
        number_of_occurrences += 1

    return number_of_occurrences == 1

for line in lines:
    [first_index, second_index, letter, password] = parse_line_2(line)

    if (is_password_valid_2(first_index, second_index, letter, password)):
        valid_passwords_count += 1

print(valid_passwords_count)

        

