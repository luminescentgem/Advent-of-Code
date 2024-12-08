from itertools import product

file = open('puzzle-7.txt')

equations = []

for line in file:
    result, *operands = line.strip().split()
    equations.append((int(result[:-1]), *list(map(int, operands))))
    
operators = [lambda x, y: x + y, lambda x, y: x * y]

def attemptEquation(operands, lambdas):
    result = operands[0]
    for i in range(len(lambdas)):
        result = lambdas[i](result, operands[i+1])
    return result

def solveEquation(equation):
    result = equation[0]
    operands = equation[1:]
    for attempt in list(product(operators, repeat=len(operands)-1)):
        if attemptEquation(operands, attempt) == result:
            return result
    return 0

print(sum(solveEquation(equation) for equation in equations))

operators.append(lambda x, y: int(str(x) + str(y)))

print(sum(solveEquation(equation) for equation in equations))