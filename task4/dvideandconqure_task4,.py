def hanoi(n, A, B, C, D):
    global total_moves
    if n == 1:
        print("Move disk 1 from", A, "to", B)
        total_moves += 1
    else:
        k = n - 1
        hanoi(k, A, C, D, B)
        print("Move disk", n, "from", A, "to", B)
        total_moves += 1
        hanoi(k, D, B, C, A)

total_moves = 0
n = 8
hanoi(n, 'A', 'B', 'C', 'D')
print("Total moves:", total_moves)
