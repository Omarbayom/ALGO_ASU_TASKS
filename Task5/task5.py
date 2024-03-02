def greedy_minimum_moves(n):
    if n % 2 != 0:
        return "No solution2"
    
    pairs = n // 2
    total_moves = 0
    remaining_moves = pairs

    for i in range(1, n+1):
        if remaining_moves <= 0:
            break
        
        if remaining_moves < i:
            moves_this_step = remaining_moves
        else:
            moves_this_step = i
        
        total_moves += moves_this_step
        remaining_moves -= moves_this_step

    return total_moves

#def can_pair(n):
#    move = 1
#    while n > move:
#        n -= move
#        move += 1
#    return n == 1

def can_pair2(n):
    move = 1
    paired = 0
    while move <= n / 2:
        paired += 1
        move += 1
        if move == n // 2 and paired % 2 != 0:
            return False
    return True


def main():
   
    MAX_VALUE = 100  
    
    for n in range(2, MAX_VALUE+1):
        if can_pair2(n) == False:
            print("For n =", n, ", minimum moves = No solution")
        else:
            print("For n =", n, ", minimum moves =", greedy_minimum_moves(n))

        
    
main()
