import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-10//example1.txt') as f:
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-10//example2.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-10//input.txt') as f:
    jolts = [int(line.rstrip()) for line in f]

jolts.sort()

jolts.insert(0, 0)
jolts.append(jolts[len(jolts) - 1] + 3)

def part_one():
    

    print(jolts)

    jolt_differences = dict()

    for i in range(0, len(jolts)-1):
        diff = jolts[i+1] - jolts[i]

        if (diff not in jolt_differences):
            jolt_differences[diff] = 0

        jolt_differences[diff] += 1

    print(jolt_differences)
    print(jolt_differences[3] * jolt_differences[1])


DP = dict()

def dp(i):
    if (i == len(jolts) - 1):
        return 1

    if (i in DP):
        return DP[i]
    
    ans = 0
    for j in range(i+1, len(jolts)):
        if (jolts[j] - jolts[i] <= 3):
            ans += dp(j)
    
    DP[i] = ans
    return ans

print(dp(0))

exit()

# retard code below

goal_jolt = jolts[-1] + 3
valid_combinations = set()

def is_valid_diff(first, next):
    diff = next - first
    return diff >= 0 and diff <= 3

def count_valid_paths(taken, remaining):
    if (len(remaining) == 0):
        if (is_valid_diff(taken[-1], goal_jolt)):
            if (taken.__str__() in valid_combinations):
                return 0

            valid_combinations.add(taken.__str__())
            return 1
        else:
            return 0

    valid_paths = 0

    for i in range(0, len(remaining)):
        next = remaining[i]
        if (not is_valid_diff(taken[-1], next)):
            continue

        valid_if_taken = count_valid_paths(taken[:] + [next], remaining[i+1:])

        valid_if_not_taken = count_valid_paths(taken[:], remaining[i+1:])

        valid_paths += valid_if_taken + valid_if_not_taken
    
    return valid_paths

result = count_valid_paths([0], jolts)
print(result)
print(len(valid_combinations))