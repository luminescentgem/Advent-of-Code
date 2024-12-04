import re
import math

num_pat = r'\d{1,3}'

pattern = fr'mul\({num_pat},{num_pat}\)'
instructions = []

filtered_pattern = fr"{pattern}|don't\(\)|do\(\)"
filtered_instructions = []

with open('puzzle-3.txt') as file:
    memory = file.read()
    instructions = re.findall(pattern, memory)
    filtered_instructions = re.findall(filtered_pattern, memory)

total = 0

for instr in instructions:
    terms = list(map(int, re.findall(num_pat, instr)))
    total += math.prod(terms)

print(total)

total = 0
enabled = True
for instr in filtered_instructions:
    
    if instr == "don't()":  enabled = False
    elif instr == "do()":   enabled = True
    elif (enabled):
        terms = list(map(int, re.findall(num_pat, instr)))
        total += math.prod(terms)

print(total)