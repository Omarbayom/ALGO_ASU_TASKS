def min_moves(n):
    memo = [0] * (n+1)
    for i in range(n-1, -1, -1):
        if (n-i) % 2 == 0:
            memo[n-i] = 2 * memo[n-i-1]
        else:
            memo[n-i] = 2 * memo[n-i-1] + 1
    return memo[n]


x = int(input("Enter the number of Swithces: "))
print("Minimum number of moves required to turn off all switches: ", min_moves(x))
