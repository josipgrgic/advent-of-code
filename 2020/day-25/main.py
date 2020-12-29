pk1 = 5764801 #card
pk2 = 17807724 #door

pk1 = 16616892 #card
pk2 = 14505727 #door

mod = 20201227

def get_loop_count(pk):
    i = 0

    subject_number = 7

    value = 1

    while value != pk:
        value = (value * subject_number) % mod
        i += 1

    return i

def transform(input, lc):
    value = 1

    for i in range(0, lc):
        value = (value * input) % mod

    return value

def part_one():
    lc1 = get_loop_count(pk1)
    lc2 = get_loop_count(pk2)

    print(lc1)
    print(lc2)

    t1 = transform(pk1, lc2)
    t2 = transform(pk2, lc1)

    print(t1)
    print(t2)

part_one()
