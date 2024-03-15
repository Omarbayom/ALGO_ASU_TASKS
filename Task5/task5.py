def greedy_pair_coin(numCoins):
    if numCoins % 2 == 0:
        n=numCoins
        moves= n//2 
        print(f"for moves:{moves} ")
        rowOfCoins = [1]*numCoins
        print(rowOfCoins)          # print(rowOfCoins)
        for i in range(1,n//4,1):         #rightside
            #1,2,.. n/4-1
                paired = False
                index_coin_we_are_jumping_to=numCoins-1    #to be paired
                while(not paired):
                    while(rowOfCoins[index_coin_we_are_jumping_to]!=1):
                        index_coin_we_are_jumping_to-=1
                    #now I have single coin
                    #let's see if we can pair it
                    numberCoinsToBeJumped=i
                    index_of_current_coin=index_coin_we_are_jumping_to-1
                    while(numberCoinsToBeJumped>0 and index_of_current_coin>=0):
                        # while I have to jump more coins ==> I deduct coins and jump them 
                        numberCoinsToBeJumped-=rowOfCoins[index_of_current_coin]
                        index_of_current_coin-=1
                    if(numberCoinsToBeJumped==0):
                        while(rowOfCoins[index_of_current_coin]<1):
                            index_of_current_coin-=1
                        if(rowOfCoins[index_of_current_coin]==1):
                            #we found exactly a coin to jump to
                            paired=True
                            rowOfCoins[index_coin_we_are_jumping_to]=2
                            rowOfCoins[index_of_current_coin]=0
                print(rowOfCoins)       
        for i in range(n//4,n//2+1,1):          #leftside
                paired = False
                index_of_current_coin=0    #to be paired
                while(not paired):
                    while(rowOfCoins[index_of_current_coin]!=1):
                        index_of_current_coin+=1
                    #now I have single coin
                    #let's see if we can pair it
                    numberCoinsToBeJumped=i
                    index_coin_we_are_jumping_to=index_of_current_coin+1
                    while(numberCoinsToBeJumped>0 and index_coin_we_are_jumping_to<=numCoins-1):
                        # while I have to jump more coins ==> I deduct coins and jump them 
                        numberCoinsToBeJumped-=rowOfCoins[index_coin_we_are_jumping_to]
                        index_coin_we_are_jumping_to+=1
                    if(numberCoinsToBeJumped==0):
                        while(rowOfCoins[index_coin_we_are_jumping_to]<1):
                            index_coin_we_are_jumping_to+=1
                        if(rowOfCoins[index_coin_we_are_jumping_to]==1):
                            #we found exactly a coin to jump to
                            paired=True
                            rowOfCoins[index_of_current_coin]=0
                            rowOfCoins[index_coin_we_are_jumping_to]=2
                    else:
                        print(f"No solution for {numCoins} Coins")
                        break
                print(rowOfCoins)
        print(rowOfCoins)
    else:
        print(f"No solution for {numCoins} Coins")


def main():
   
    i = int(input("please enter even number of N's: "))
    greedy_pair_coin(i)

if __name__ == "__main__":
    main()

