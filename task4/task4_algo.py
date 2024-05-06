import math

moveCount = 0

def four_pegs(n, p, q, r, s):
    global moveCount
    if n == 0:
        return

    if n == 1:
        print("Move disk 1 from rod", p, "to rod", q)
        moveCount += 1
        return

    four_pegs(n - 2, p, r, s, q)

    print("Move disk", n - 1, "from rod", p, "to rod", s)
    print("Move disk", n, "from rod", p, "to rod", q)
    print("Move disk", n - 1, "from rod", s, "to rod", q)
    moveCount += 3

    four_pegs(n - 2, r, q, p, s)

def three_pegs(m, p, q, r):
    global moveCount
    if m == 1:
        print("Move disk 1 from rod", p, "to rod", q)
        moveCount += 1
        return
    three_pegs(m - 1, p, r, q)
    print("Move disk", m, "from rod", p, "to rod", q)
    moveCount += 1
    three_pegs(m - 1, r, q, p)

def four_three_pegs(i, j, a, b, c, d):
    global moveCount
    m = j - i + 1
    k = int(math.sqrt(2 * m))
    print("**Here we will start by moving first smallest", k, "disks within the 4 pegs(A, B, C, D)")
    four_pegs(m - k, a, c, b, d)
    print("**rest of disks will move within the 3 pegs(A, B, D) excluding the peg 'C'")
    three_pegs(k, a, d, b)
    print("**then returning the first moved disks on top of the remaining disks")
    four_pegs(m - k, c, d, a, b)

if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    print()
    four_three_pegs(1, n, 'A', 'B', 'C', 'D')
    print("Total moves:", moveCount)
