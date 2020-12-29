import functools 

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-06//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-06//input.txt') as f:
    lines = [line.rstrip() for line in f]

lines.append('')

global_yes_per_group = []

yes_answers_frequency = dict()
people_in_group = 0

for line in lines:
    if (line != ''):
        people_in_group += 1

        for char in line:
            if (char not in yes_answers_frequency):
                yes_answers_frequency[char] = 0

            yes_answers_frequency[char] += 1
        
        continue

    
    print(yes_answers_frequency)

    global_yes_in_group = 0
    for answer, frequency in yes_answers_frequency.items():
        if (frequency == people_in_group):
            global_yes_in_group += 1

    global_yes_per_group.append(global_yes_in_group)
    people_in_group = 0
    yes_answers_frequency = dict()

print(global_yes_per_group)
sum = functools.reduce(lambda a,b: a + b, global_yes_per_group)
print(sum)
