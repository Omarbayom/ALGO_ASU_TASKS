def append_lists(list1, list2):
    for i in range(len(list2)):
        list1.append(list2[i])
    return list1

def print_switches(n, M):
    switches = [1 for _ in range(n)]
    print(switches)
    for i in M[n]:
        if switches[i] == 1:
            switches[i] = 0
        else:
            switches[i] = 1
        print(switches)

def security_switches(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    MToCloseSet = [[] for _ in range(n + 1)]
    MToCloseSet[1], MToCloseSet[2] = [n-1], [n-2, n-1]
    
    MToCloseSwitch = [[] for _ in range(n + 1)]
    MToCloseSwitch[1], MToCloseSwitch[2] = [n-1], [n-1, n-2, n-1]

    MToOpenSwitch = [[] for _ in range(n + 1)]
    MToOpenSwitch[1], MToOpenSwitch[2] = [n-1], [n-1, n-2, n-1]


    for i in range(3, n + 1):
        MToCloseSet[i] = MToCloseSet[i-2]
        MToCloseSet[i].append(n-i)
        if (i == 3):
            append_lists(MToCloseSet[i], MToCloseSwitch[2])
        else:
            MToOpenSwitch[i-2] = []
            if(not MToOpenSwitch[i-2]):
                append_lists(MToOpenSwitch[i-2], MToOpenSwitch[i-3])
                MToOpenSwitch[i-2].append(n - i + 2)
                append_lists(MToOpenSwitch[i-2], MToCloseSwitch[i-3])
            append_lists(MToCloseSwitch[i-1], MToOpenSwitch[i-2])
            MToCloseSwitch[i-1].append(n - i + 1)
            append_lists(MToCloseSwitch[i-1], MToCloseSwitch[i-2])
            append_lists(MToCloseSet[i], MToCloseSwitch[i-1])

    print_switches(n, MToCloseSet)
    return len(MToCloseSet[n])

print(security_switches(6))
