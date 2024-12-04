safe_reports = 0

reports = []

with open('puzzle-2.txt') as file:
    for line in file:
        reports.append(list(map(int, line.split(' '))))


# Check for all 3 levels
for data in reports:    
    if (
            len(data) == len(set(data)) # No duplicates
        and (sorted(data) == data or sorted(data) == data[::-1]) # Decreasing or increasing order
        and max(abs(data[i+1] - data[i]) for i in range(len(data)-1)) <= 3 # Max distance of 3
    ):
        safe_reports += 1

print(safe_reports)

# Reset for part 2
safe_reports = 0

for data in reports:
    safe = lambda l : len(l) == len(set(l)) and (sorted(l) == l or sorted(l) == l[::-1]) and max(abs(l[i+1] - l[i]) for i in range(len(l)-1)) <= 3
    
    if safe(data):
        safe_reports += 1
    else:
        for i in range(len(data)):
            if safe(data[0:i] + data[i+1:]):
                safe_reports += 1
                break

print(safe_reports)
