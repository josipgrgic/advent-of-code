
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-15//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-15//input.txt') as f:
    lines = [line.rstrip() for line in f]

#https://oeis.org/A181391

def part_one(numbers):
    turn = 1
    number_dict = dict()
    last_number = -1

    def say_number(number, turn):
        if (number not in number_dict):
            number_dict[number] = [turn]
        elif (len(number_dict[number]) == 1):
            number_dict[number].append(turn)
        else:
            number_dict[number] = [number_dict[number][1], turn]

    for n in numbers:
        say_number(n, turn)
        last_number = n
        turn += 1

    while turn <= 30000000:
        number_to_say = 0

        if (len(number_dict[last_number]) == 2):
            number_to_say = number_dict[last_number][1] - number_dict[last_number][0]

        say_number(number_to_say, turn)
        last_number = number_to_say
        turn += 1

    print(last_number)

def part_two(numbers):
    turn = 1
    limit = 30000000

    number_occurrences = [-1] * (limit + 1)

    last_number = -1

    for n in numbers:
        number_occurrences[n] = turn
        last_number = n
        turn += 1

    while turn <= limit:
        new_number = 0
        
        if (number_occurrences[last_number] != -1):
           new_number = turn - 1 - number_occurrences[last_number]

        number_occurrences[last_number] = turn - 1
        last_number = new_number
        turn += 1

    print(last_number)

for line in lines:
    numbers = [int(n) for n in line.split(',')]
    part_two(numbers)

