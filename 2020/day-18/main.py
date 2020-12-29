
#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-18//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-18//input.txt') as f:
    lines = [line.rstrip() for line in f]

class Expression:
    def __init__(self, arr):
        self.arr = arr
    
    def resolve(self, dict):
        result = self.get_value(self.arr[0], dict)

        for i in range(1, len(self.arr), 2):
            right =  self.arr[i+1]
            operation = self.arr[i]

            r_value = self.get_value(right, dict)

            if (operation == '+'):
                result +=  r_value
            else:
                result *= r_value

        return result

    def resolve2(self, a, dict):
        result = self.get_value(a[0], dict)

        for i in range(1, len(a), 2):
            right =  a[i+1]
            operation = a[i]

            r_value = self.get_value(right, dict)

            if (operation == '+'):
                result +=  r_value
            else:
                result *= r_value

        return result

    def resolve3(self, dict):
        
        result = 1

        str = ''.join(self.arr)
        a = str.split('*')

        for el in a:
            l = list(el)
            value = self.resolve2(l, dict)
            result *= value

        return result

    def get_value(self, value, dict):
        if (value.isnumeric()):
            return int(value)
        else:
            return dict[value].resolve3(dict)


def create_array(line):
    arr = []
    splitted = list(line)
    for char in splitted:
        if (char != ' '):
            arr.append(char)
    return arr

def create_expression(arr, dict):
    expression_array = []
    i = 0
    while i < len(arr):
        char = arr[i]

        if (char != '('):
            expression_array.append(char)
            i += 1
            continue

        num_of_parantheses = 1
        i += 1
        inner_expression_array = []
        while (num_of_parantheses != 0):
            inner_char = arr[i]
            i += 1
            if (inner_char != '(' and inner_char != ')'):
                inner_expression_array.append(inner_char)
            elif (inner_char == '('):
                num_of_parantheses += 1
                inner_expression_array.append(inner_char)
            else:
                num_of_parantheses -= 1
                if (num_of_parantheses != 0):
                    inner_expression_array.append(inner_char)

        inner_expression = create_expression(inner_expression_array, dict)
        inner_expression_key = chr(ord('a') + len(dict))
        dict[inner_expression_key] = inner_expression
        expression_array.append(inner_expression_key)
    
    expression = Expression(expression_array)
    return expression

def part_one():
    result = 0

    for line in lines:
        dict = {}
        arr = create_array(line)
        expression = create_expression(arr, dict)
        value = expression.resolve3(dict)
        print(value)
        result += value

    print(result)

part_one()

def part_two():
    pass


