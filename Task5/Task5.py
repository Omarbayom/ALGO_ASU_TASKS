def greedy_pair_coins(lstOfN):
    for n in lstOfN:
        lst = [1] *n
        move = 1
        total_moves = 0
        pairs = 0
        for i in range (0,n-1):
            if lst[i] ==2 or lst[i] == 0:
                continue
            next_move = i +move
            altnext_move = i-move
            flag = True
            if flag == True:
                j = i
                while j != next_move:
                    if j > n-1:
                        break
                    if lst[j] == 0:
                        next_move +=1
                    elif lst[j] ==2:
                        next_move-=1
                    j+=1

                if next_move <=n-1 and lst[next_move] ==1:
                    lst[next_move] +=1
                    pairs+=1
                    lst[i] = 0
                    total_moves +=move
                    move+=1
                else:
                    flag = False
                
            elif flag == False: 
                j = i
                while j != altnext_move:
                    if j < 0:
                        break
                    if lst[j] == 0:
                        altnext_move -=1
                    elif lst[j] ==2:
                        altnext_move+=1
                    j-=1

                if altnext_move>=0 and lst[altnext_move] ==1:
                    lst[altnext_move] +=1
                    pairs+=1
                    lst[i] = 0
                    total_moves +=move
                    move+=1
        if n %2 == 0 and pairs == n//2:
            print(f"for n = {n} has a solution and with total moves = {total_moves}")
            print(lst)
        else:
            print(f"for n = {n} has no solution")
                


def main():
   
    lstOfNs = []
    for i in range(2,101,2):
        lstOfNs.append(i)
    greedy_pair_coins(lstOfNs)

        
    
main()