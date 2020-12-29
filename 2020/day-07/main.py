import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-07//example.txt') as f:
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-07//example2.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-07//input.txt') as f:
    lines = [line.rstrip() for line in f]

class BagRule(object):
    def __init__(self, bag, amount):
        self.bag = bag
        self.amount = amount

    def __repr__(self):
        return "{0} {1} bags".format(self.amount, self.bag)

    def __str__(self):
        return "{0} {1} bags".format(self.amount, self.bag)

bag_rules = dict()

for line in lines:
    m = re.search(r"(.*) bags contain (.*).", line)

    (main_bag, content) = m.groups()
    
    inner_bags = content.split(',')

    if (len(inner_bags) == 1 and inner_bags[0] == 'no other bags'):
        continue

    list = []
    
    for bag in inner_bags:
        m = re.search(r"\s*([1-9][0-9]*) (.*) bag", bag)
        (num_str, bag_color) = m.groups()

        num = int(num_str)

        list.append(BagRule(bag_color, num))

    bag_rules[main_bag] = list

print(bag_rules)

target = 'shiny gold'
colors_that_contain_target = set()

def does_eventually_contain_target(bag):
    if (bag not in bag_rules):
        return False

    if (bag in colors_that_contain_target):
        return True

    rules = bag_rules[bag]

    for rule in rules:
        if (rule.bag == target):
            colors_that_contain_target.add(bag)
            return True

    for rule in rules:
        if (does_eventually_contain_target(rule.bag)):
            colors_that_contain_target.add(bag)
            return True

    return False

def count_colors_that_eventually_have_target(target):
    for bag in bag_rules.keys():
        does_eventually_contain_target(bag)
    print(len(colors_that_contain_target))

total_inner_bags_count_per_bag = dict()
list = []

def count_total_inner_bags_recursively(target):
    if (target not in bag_rules):
        return 0
    
    if (target in total_inner_bags_count_per_bag):
        list.append(1)
        return total_inner_bags_count_per_bag[target]

    rules = bag_rules[target]
    total = 0

    for rule in rules:
        total += rule.amount
        child_total = count_total_inner_bags_recursively(rule.bag)
        total += rule.amount * child_total
    
    total_inner_bags_count_per_bag[target] = total

    return total

total = count_total_inner_bags_recursively(target)

print(total_inner_bags_count_per_bag)
print(len(list))
print(total)

