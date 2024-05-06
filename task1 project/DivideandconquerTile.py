def tile(n, x, y, location):
    global counter, arr

    if n == 2:
        counter += 1
        for i in range(n):
            for j in range(n):
                if arr[x + i][y + j] == 0:
                    if location == "up right" or location == "down left":
                        arr[x + i][y + j] = 'w'
                    elif location == "down right" or location == "up left":
                        arr[x + i][y + j] = 'b'
        return

    # finding hole location
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != 0:
                r, c = i, j

    # If missing tile is up right
    if r < x + n // 2 and c < y + n // 2:
        counter += 1
        arr[x + n // 2][y + (n // 2) - 1] = 'g'
        arr[x + n // 2][y + n // 2] = 'g'
        arr[x + n // 2 - 1][y + n // 2] = 'g'

    # If missing Tile is in down left
    elif r >= x + n // 2 and c < y + n // 2:
        counter += 1
        arr[x + (n // 2) - 1][y + (n // 2)] = 'g'
        arr[x + (n // 2)][y + n // 2] = 'g'
        arr[x + (n // 2) - 1][y + (n // 2) - 1] = 'g'

    # If missing Tile is in up left
    elif r < x + n // 2 and c >= y + n // 2:
        counter += 1
        arr[x + n // 2][y + (n // 2) - 1] = 'g'
        arr[x + n // 2][y + n // 2] = 'g'
        arr[x + (n // 2) - 1][y + (n // 2) - 1] = 'g'

    # If missing Tile is in down right
    elif r >= x + n // 2 and c >= y + n // 2:
        counter += 1
        arr[x + (n // 2) - 1][y + (n // 2)] = 'g'
        arr[x + n // 2][y + (n // 2) - 1] = 'g'
        arr[x + (n // 2) - 1][y + (n // 2) - 1] = 'g'

    # dividing it again in 4 quadrants
    tile(n // 2, x, y + n // 2, "down left")
    tile(n // 2, x, y, "down right")
    tile(n // 2, x + n // 2, y, "up right")
    tile(n // 2, x + n // 2, y + n // 2, "up left")


size_of_grid = int(input("Enter the size of the grid (n): "))

arr = [[0] * 128 for _ in range(128)]
counter = 0
missing_row = int(input("Enter the row number of the missing tile: "))
missing_col = int(input("Enter the column number of the missing tile: "))
arr[missing_row][missing_col] = 'x'
tile(size_of_grid, 0, 0, "up right")

for i in range(size_of_grid):
    for j in range(size_of_grid):
        print(arr[i][j], end=" ")
    print()
