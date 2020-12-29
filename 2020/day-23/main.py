
input = '389125467'
input = '583976241'

moves = 10000000

cups = [int(x) for x in list(input)]
m = max(cups)
min = min(cups)

for i in range(m + 1, 1000001):
    cups.append(i)

m = 1000000

dict = {}

class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        
current_node = Node(cups[0])
temp = current_node

dict[cups[0]] = current_node

for i in range(1, len(cups)):
    next = Node(cups[i])
    dict[cups[i]] = next
    #next.prev = temp
    temp.next = next
    temp = next

temp.next = current_node
#current_node.prev = temp

def pop_circular(list, index):
    return list.pop(index % len(list))

def part_one():
    global cups
    global current_node
    global moves
    print('start')

    for i in range(0, moves):
        if (i % 1000000 == 0):
            print(i)

        three_cups = current_node.next
        three_cup_list = [three_cups.value, three_cups.next.value, three_cups.next.next.value]

        current_node.next = current_node.next.next.next.next

        destination_cup = current_node.value
        while True:
            destination_cup -= 1

            if destination_cup < min:
                destination_cup = m

            if destination_cup not in three_cup_list:
                break
        
        destination_node = dict[destination_cup]

        three_cups.next.next.next = destination_node.next
        destination_node.next = three_cups

        current_node = current_node.next

    one_cup = dict[1]

    n1 = one_cup.next
    n2 = one_cup.next.next

    print(n1.value)
    print(n2.value)

    print(n1.value * n2.value)


part_one()

def part_two():
    global cups
    global current_cup
    global moves

    for i in range(0, moves):

        if (i % 1000 == 0):
            print(i)

        #print('-- move {} --'.format(i + 1))
        #print(cups)
        #print(current_cup)
        destination_cup = current_cup
        three_cups = [pop_circular(cups, cups.index(current_cup) + 1), pop_circular(cups, cups.index(current_cup) + 1), pop_circular(cups, cups.index(current_cup) + 1)]
        #print(three_cups)
        while True:
            destination_cup -= 1

            if destination_cup < min:
                destination_cup = m

            if destination_cup not in three_cups:
                break
        
        #print(destination_cup)
        destination_index = cups.index(destination_cup) + 1

        for i in range(2, -1, -1):
            cups.insert(destination_index, three_cups[i])

        current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]

    one_index = cups.index(1)

    index = (one_index + 1) % len(cups)

    #str = ''
    #while index != one_index:
    #    str += '{}'.format(cups[index])
    #    index = (index + 1) % len(cups)

    #print(str)

    n1 = cups[one_index + 1]
    n2 = cups[one_index + 2]

    print(n1)
    print(n2)

    print(n1 * n2)


