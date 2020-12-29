
import re
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-16//example.txt') as f:
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-16//example2.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-16//input.txt') as f:
    lines = [line.rstrip() for line in f]

rules = dict()
ranges = []
line_number = 0
valid_tickets = []

while lines[line_number] != '':
    [rule, l1, u1, l2, u2] = re.match(r"(.*): (.*)-(.*) or (.*)-(.*)", lines[line_number]).groups()
    rules[rule] = (int(l1), int(u1), int(l2), int(u2))
    ranges.append((int(l1), int(u1)))
    ranges.append((int(l2), int(u2)))
    line_number += 1

print(rules)

my_ticket = [int(n) for n in lines[line_number + 2].split(",")]

line_number += 5

def part_one():
    sum = 0
    for i in range(line_number, len(lines)):
        ticket = [int(n) for n in lines[i].split(",")]
        is_ticket_valid = True
        for value in ticket:
            is_valid = False
            for value_range in ranges:
                if (value >= value_range[0] and value <= value_range[1]):
                    is_valid = True
                    break
            
            if (not is_valid):
                is_ticket_valid = False
                sum += value

        if (is_ticket_valid):
            valid_tickets.append(ticket)

    print(sum)

part_one()

print(valid_tickets)

def part_two():
    ticket_fields = []

    for val in rules.keys():
        ticket_fields.append(list(rules.keys()))

    print(ticket_fields)

    for ticket in valid_tickets:
        for i in range(0, len(ticket)):
            if (len(ticket_fields[i]) == 1):
                continue
            
            value = ticket[i]

            new_fields = []
            old_fields = ticket_fields[i]

            for j in range(0, len(old_fields)):
                rule = rules[old_fields[j]]
                if ((value >= rule[0] and value <= rule[1]) or (value >= rule[2] and value <= rule[3])):
                    new_fields.append(old_fields[j])

            ticket_fields[i] = new_fields

            if (len(new_fields) != 1):
                continue
            
            cleared_values = [new_fields[0]]

            while len(cleared_values) > 0:
                new_cleared_values = []

                for j in range(0, len(ticket_fields)):
                    if (len(ticket_fields[j]) == 1):
                        continue

                    ticket_fields[j] = list(filter(lambda x: x not in cleared_values, ticket_fields[j]))

                    if (len(ticket_fields[j]) == 1):
                        new_cleared_values.append(ticket_fields[j][0])
                    
                cleared_values = new_cleared_values

    print(ticket_fields)

    prod = 1
    for i in range(0,len(my_ticket)):
        if (ticket_fields[i][0].startswith("departure")):
            prod *= my_ticket[i]

    print(prod)

part_two()
