import itertools

string='1?2?3'

def operation_counter(string):
    count = 0
    for i in string:
        if (i == '?'):
            count += 1
        else:
            pass
    return count

def q_positions(string):
    positions = []
    for i in range(len(string)):
        if (string[i] == '?'):
            positions.append(i)
    return positions

def string_char_replacer(string,newstring,index):
    string = string[:index] + newstring + string[index + 1:]
    return string

def parenthesize(string):
    operators = ['?']
    depth = len([s for s in string if s in operators])
    if depth == 0:
        return [string]
    if depth== 1:
        return ['('+ string + ')']
    answer = []
    for index, symbol in enumerate(string):
        if symbol in operators:
            left = string[:index]
            right = string[(index+1):]
            strings = ['(' + lt + ')' + symbol +'(' + rt + ')'
                           for lt in parenthesize(left)
                           for rt in parenthesize(right) ]
            answer.extend(strings)
    return answer

def operation_replacer(string):
    opr = ['+', '-', '*', '/']
    operation_numbers = operation_counter(string)
    products = list(itertools.product(opr, repeat=operation_numbers))
    #print(products)
    return products


def single_operation_list(string):
    single_operators = []
    for i in range(len(string)):
        char = string[i]
        if (char == "'" and string[i+1] != "," and  string[i+1] != ")"):
            single_operator = string[i+1:i+2]
            single_operators.append(single_operator)
    return single_operators

exp= parenthesize(string)
opr_tuple = operation_replacer(string)

opr = []
for i in opr_tuple:
    tuple = str(i).replace(' ', '')
    opr.append(tuple)


for i in exp:
    for j in opr:
        h = single_operation_list(j)
        spare = i
        for l in h:
            i = i.replace('?',l,1)
            find_q = i.find('?')
            if (find_q == -1):
                try:
                    evaluation = str(eval(i))
                except ZeroDivisionError:
                    evaluation = 'Division By Zero!'
                print(i + ' = ' + evaluation)
            else:
                pass
        i = spare
