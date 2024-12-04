l1, l2 = [], []
with open('puzzle-1.txt') as file:
    for line in file:
        terms = line.split(' ')
        l1.append(int(terms[0]))
        l2.append(int(terms[3]))

# Sort the lists
l1.sort()
l2.sort()

distances = []

# Calculate distances
for i in range(len(l1)):
    distances.append(abs(int(l1[i]) - int(l2[i])))

print(sum(distances))

similarities = []
for n in l1:
    similarities.append(n * l2.count(n))

print(sum(similarities))