file = open('puzzle-6.txt')

width = 0
height = 0

board = []
for line in file:
    width = len(line)
    height += 1
    board = [*board + list(line.strip())]

original_board = board.copy()

def getCell(x, y):
    # Cell (y, x)
    return False if 0 > x or x >= width or 0 > y or y >= height else board[y*width+x]

def setCell(x, y, val):
    # Cell (y, x)
    if 0 > x >= width or 0 > y >= height:
        return False 
    board[y * width + x] = val
    return True

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def printBoard(b):
    print()
    for i in range(height-1):
        print(''.join(board[i*width:(i+1)*width]))
    print()

def runStraight(x, y, direction):
    x_inc = directions[direction][0]
    y_inc = directions[direction][1]

    while True:   
        cell = getCell(x+x_inc, y+y_inc)
        # print(cell)
        # print(x, y)
        # print(direction)
        # print()
        if not cell:
            return False, False

        if cell != '#':
            x, y = x+x_inc, y+y_inc
            setCell(x, y, 'X')
        else:
            return x, y

def simulateGuard():
    i = board.index('^')
    x = i % width
    y = int(i / width)
    setCell(x, y, 'X')
    direction = 3 #top

    history = [(x, y, direction)]
    
    while(True):
        history.append(0)
        history[-1] = (x, y, direction)
        
        x, y = runStraight(x, y, direction)
        
        direction = (direction + 1) % 4
        
        if (x, y, direction) in history[:-1]:
            setCell(x, y, '§')
            return False
        
        if (x == False and y == False):
            return board.count('X')

board = original_board.copy()
print(simulateGuard())

loops = 0
for i in range(len(original_board)):
    if original_board[i] != '.':
        continue
    
    board = original_board.copy()
    board[i] = '#'
    
    if not simulateGuard():
        #printBoard(board)
        loops += 1

print(loops)