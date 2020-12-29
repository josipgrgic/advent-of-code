import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-04//valid.txt') as f:
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-04//invalid.txt') as f:

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-04//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-04//input.txt') as f:
    lines = [line.rstrip() for line in f]

lines.append('eof')

birth_year = 'byr'
issue_year = 'iyr'
expiration_year = 'eyr'
height = 'hgt'
hair_color = 'hcl'
eye_color = 'ecl'
passport_id = 'pid'
country_id = 'cid'

valid_password_count = 0
single_passport_lines = []

def validate_birth_year(value):
    m = re.search(r"(^([0-9]|[1-9][0-9]*)$)", value)

    if (m is None):
        print('invalid birth_year')
        return False

    num = int(m.group(1))
    if (num >= 1920 and num <= 2002):
        return True

    print('invalid birth_year')
    return False

def validate_issue_year(value):
    m = re.search(r"(^([0-9]|[1-9][0-9]*)$)", value)

    if (m is None):
        print('invalid issue_year')
        return False

    num = int(m.group(1))
    if (num >= 2010 and num <= 2020):
        return True

    print('invalid issue_year')
    return False

def validate_expiration_year(value):
    m = re.search(r"(^([0-9]|[1-9][0-9]*)$)", value)

    if (m is None):
        print('invalid expiration_year')
        return False

    num = int(m.group(1))
    if (num >= 2020 and num <= 2030):
        return True

    print('invalid expiration_year')
    return False

def validate_height(value):
    m = re.search(r"([1-9][0-9]*)(\w+)", value) 

    if (m is None):
        print('invalid height')
        return False

    (size_str, unit) = m.groups()
    size = int(size_str)

    if (unit == 'cm' and size >= 150 and size <= 193):
        return True
    if (unit == 'in' and size >= 59 and size <= 76):
        return True

    print('invalid height')
    return False

def validate_hair_color(value):
    m = re.search(r"^#([a-f]|[0-9]){6}$", value)
    if (m is not None):
        return True
    
    print('invalid hair_color')
    return False

def validate_eye_color(value):
    return value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth'

def validate_passport_id(value):
    if (len(value) == 9 and value.isnumeric()):
        return True

    print('invalid passport_id')
    return False

for line in lines:
    if (line != '' and line != 'eof'):
        single_passport_lines.append(line)
        continue

    current_passport_data = ' '.join(single_passport_lines)
    print(current_passport_data)

    passport_dict = {}

    for [key, value] in [kvp.split(':') for kvp in current_passport_data.rstrip().split(' ')]:
        passport_dict[key] = value

    single_passport_lines = []

    if (len(passport_dict) < 7 or (len(passport_dict) == 7 and country_id in passport_dict)):
        print('missing data')
        continue

    isValid = True

    isValid &= validate_birth_year(passport_dict[birth_year])
    isValid &= validate_issue_year(passport_dict[issue_year])
    isValid &= validate_expiration_year(passport_dict[expiration_year])
    isValid &= validate_height(passport_dict[height])
    isValid &= validate_hair_color(passport_dict[hair_color])
    isValid &= validate_eye_color(passport_dict[eye_color])
    isValid &= validate_passport_id(passport_dict[passport_id])

    if (isValid):
        valid_password_count += 1
        print('valid')
        continue

    print('invalid')

print(valid_password_count)
