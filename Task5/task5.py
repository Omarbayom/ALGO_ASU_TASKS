def greedy_minimum_moves(n):
    if n % 2 != 0 or (n // 2) % 2 == 0:
        return "No solution"
    
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

def main():
    valid_n_values = []
    
    MAX_VALUE = 100  
    
    for n in range(2, MAX_VALUE+1):
        if n % 2 == 0 and (n // 2) % 2 != 0:
            valid_n_values.append(n)
    
    for n in valid_n_values:
        moves = greedy_minimum_moves(n)
        print("For n =", n, ", minimum moves =", moves)

main()