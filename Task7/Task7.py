import random

memo = {} 

def randmove(target_position, n):
    if target_position == 1:
        return target_position + 1
    elif target_position == n:
        return target_position - 1
    
    x = random.randint(0, 1)

    if x == 0:
        target_position += 1
    else:
        target_position -= 1

    return target_position

def simulate_game(n):
    target_position = random.randint(1, n)
    shots = 0
    j = 1
    hits = []  
    
    if target_position in memo: 
        return memo[target_position]
    
    for i in range(2, n, 1):
        hits.append((i, target_position))
        shots += 1
        if i == target_position:
            memo[target_position] = (shots, hits)
            return shots, hits
        else:
            target_position = randmove(target_position, n)
            j += 1

    for i in range(n - 1, 1, -1):
        hits.append((i, target_position))
        shots += 1
        if i == target_position:
            memo[target_position] = (shots, hits)
            return shots, hits
        else:
            target_position = randmove(target_position, n)
            j += 1

    return shots, hits

# Test the function
n = 5
shots, hits = simulate_game(n)
print("Number of shots taken to hit the target for n =", n, "is", shots)
print("Hits:", hits)