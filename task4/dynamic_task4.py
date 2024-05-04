def int_to_string(n):
    return str(n)

def tower_of_hanoi_4_pegs(n, A, B, C, D):
    memo = {}

    def helper(n, A, B, C, D):
        if n == 0:
            return 0

        key = int_to_string(n) + A + B + C + D
        if key in memo:
            return memo[key]

        moves = 0

        if n == 1:
            print("Move disk 1 from rod", A, "to rod", B)
            return 1

        moves += helper(n - 2, A, C, D, B)
        print("Move disk", n - 1, "from rod", A, "to rod", D)
        print("Move disk", n, "from rod", A, "to rod", B)
        print("Move disk", n - 1, "from rod", D, "to rod", B)
        moves += 3

        moves += helper(n - 2, C, B, A, D)

        memo[key] = moves
        return moves

    return helper(n, A, B, C, D)

def main():
    n = int(input("Enter the number of disks: "))
    total_moves = tower_of_hanoi_4_pegs(n, 'A', 'D', 'B', 'C')
    print("Total moves:", total_moves)

if __name__ == "__main__":
    main()
