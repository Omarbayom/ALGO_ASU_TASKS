def _4_pegs(n, A, B, C, D):
    global total_moves
    
    if (n == 0):
        return
    if (n == 1):
        print("Move disk", n, "from rod", A, "to rod", B)
        total_moves += 1
        return

    _4_pegs(n - 2, A, C, D, B)
    total_moves += 3

    print("Move disk", n - 1, "from rod", A, "to rod", D)
    print("Move disk", n, "from rod", A, "to rod", B)
    print("Move disk", n - 1, "from rod", D, "to rod", B)

    _4_pegs(n - 2, C, B, A, D)

n = int(input("Enter the number of disks: "))
total_moves = 0
_4_pegs(n, 'A', 'D', 'B', 'C')
print("Total moves:", total_moves)

