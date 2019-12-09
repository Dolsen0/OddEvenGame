from random import randint

g = [1, 2]

comp_move = g[randint(0, 1)]
player = False


while player == False:
    player = input("Do you choose 1 or 2?")
    
    move = int(player) + int(comp_move)
    
    print("I choose", comp_move)
    
    
    if move % 2 == 0:
        print("Even")
    else:
        print("Odd")
    print(move)
    player = False
