moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2],
         [1, -2], [1, 2], [2, -1], [2, 1]]

def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def get_unvisited_neighbors(board, x, y):
    count = 0
    for move in moves:
        dx, dy = move
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and board[ny][nx] == 0:
            count += 1
    return count

def get_next_move(board, x, y):
    min_neighbors = 8
    next_x, next_y = -1, -1
    for move in moves:
        dx, dy = move
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and board[ny][nx] == 0:
            unvisited_neighbors = get_unvisited_neighbors(board, nx, ny)
            if unvisited_neighbors < min_neighbors:
                min_neighbors = unvisited_neighbors
                next_x, next_y = nx, ny
    return next_x, next_y

def display_board(board, x, y):
    for i in range(8):
        for j in range(8):
            if i == y and j == x:
                print(' K', end=' ')
            else:
                print('{:2}'.format(board[i][j]), end=' ')
        print()


def knight_tour():
    for start_x in range(8):
        for start_y in range(8):
            print(f"Trying starting position ({start_x}, {start_y})...")
            board = [[0 for _ in range(8)] for _ in range(8)]
            x, y = start_x, start_y
            board[y][x] = 1
            wohx, wohy = x, y
            
            for i in range(2, 65):
                x, y = get_next_move(board, x, y)
                board[y][x] = i
                if i == 64:
                    if [wohx, wohy] not in [[x + dx, y + dy] for dx, dy in moves]:
                        break
                    else:
                        print("Knight's tour completed!")
                        display_board(board, x, y)


knight_tour()
