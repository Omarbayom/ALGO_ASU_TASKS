def security_switches(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    M = []
    for i in range(n + 1):
        M.append(0)
    M[1], M[2] = 1, 2
    
    for i in range(3, n + 1):
        M[i] = M[i - 1] + 2 * M[i - 2] + 1
    
    return M[n]

print(security_switches(4))
