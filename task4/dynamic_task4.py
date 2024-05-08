def int_to_string(n):
    return str(n)

def dynamic_4_pegs(n, A, B, C, D):
    memo = {}

    def helper(n, A, B, C, D):
        if n == 0:
            return 0

        key = int_to_string(n) + A + B + C + D
        if key in memo:
            print("*reusing is done here*")
            return memo[key]

        moves = 0

        if n == 1:
            print("Move disk 1 from rod", A, "to rod", B)
            return 1

        moves += helper(n - 2, A, C, D, B) # move first n-2 disks from A to C using (D and B )as auxiliary rods
        print("Move disk", n - 1, "from rod", A, "to rod", D)
        print("Move disk", n, "from rod", A, "to rod", B)
        print("Move disk", n - 1, "from rod", D, "to rod", B)
        moves += 3

        moves += helper(n - 2, C, B, A, D)  # move n-2 disks from  C to B using (A and D )as auxiliary rods

        memo[key] = moves
        return moves

    return helper(n, A, B, C, D)

def main():
    n = int(input("Enter the number of disks: "))
    total_moves = dynamic_4_pegs(n, 'A', 'D', 'B', 'C')
    print("Total moves:", total_moves)

if __name__ == "__main__":
        main()
