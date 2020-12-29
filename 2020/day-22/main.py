
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-22//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-22//input.txt') as f:
    lines = [line.rstrip() for line in f]

player_1 = []
player_2 = []

def load_cards():
    global player_1
    global player_2

    p1 = True

    for line in lines:
        if line == 'Player 2:':
            p1 = False
            continue
        if not line.isnumeric():
            continue

        if p1:
            player_1.append(int(line))
        else:
            player_2.append(int(line))

load_cards()

def part_one():
    while len(player_1) > 0 and len(player_2) > 0:
        p1 = player_1.pop(0)
        p2 = player_2.pop(0)

        if (p1 > p2):
            player_1.append(p1)
            player_1.append(p2)
        else:
            player_2.append(p2)
            player_2.append(p1)

    wining = None

    if len(player_1) > 0:
        wining = player_1
    else:
        wining = player_2

    result = 0

    for i in range(0, len(wining)):
        result += wining[i] * (len(wining) - i)

    print(result)

def join_cards(numbers):
    return ",".join("'{0}'".format(n) for n in numbers)

def play_game(player1, player2):
    played_games = set()

    while len(player1) > 0 and len(player2) > 0:
        cards = '{}-{}'.format(join_cards(player1), join_cards(player2))

        if cards in played_games:
            print('Player 1 auto win')
            return 1
        
        played_games.add(cards)

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        res = 0
        if len(player1) >= p1 and len(player2) >= p2:
            res = play_game(player1[:p1], player2[:p2])

        if res > 0:
            if res == 1:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
            
            continue

        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    if len(player1) > 0:
        return 1
    else:
        return 2

def part_two():
    global player_1
    global player_2

    res = play_game(player_1, player_2)

    wining = None

    if res == 1:
        wining = player_1
    else:
        wining = player_2

    result = 0

    for i in range(0, len(wining)):
        result += wining[i] * (len(wining) - i)

    print(result)

part_two()


