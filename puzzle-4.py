file = open('puzzle-4.txt')

WORD = 'XMAS'
SIZE = len(WORD)

board = [line.strip() for line in file]

directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

# Function to check "XMAS" in all directions
def check(x, y, direction):
    last_coords = directions[direction]

    # Boundary checks
    if not (0 <= x + last_coords[1] * (SIZE - 1) < len(board)):  # Y-axis
        return False
    if not (0 <= y + last_coords[0] * (SIZE - 1) < len(board[0])):  # X-axis
        return False

    # Extract word
    word = ''.join(board[x + i * last_coords[1]][y + i * last_coords[0]] for i in range(SIZE))
    return word == WORD

# Count occurrences of "XMAS"
occurrences = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        for n in range(len(directions)):
            if check(j, i, n):
                occurrences += 1

print(occurrences)


# Function to check the "X" pattern
def checkX(x, y):
    if not (board[x][y] == 'A') \
            or not (1 <= x < len(board) - 1)   \
            or not (1 <= y < len(board[0]) - 1):
        return False

    try:
        # Extract diagonals
        diag = ''.join(board[x + i][y + i] for i in (-1, 0, 1))
        rev_diag = ''.join(board[x + i][y - i] for i in (-1, 0, 1))

        # Check for matching patterns
        return diag in ('SAM', 'MAS') and rev_diag in ('SAM', 'MAS')
    except IndexError:
        return False

# Count occurrences of the "X" pattern
occurrences = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if checkX(i, j):
            occurrences += 1

print(occurrences)
