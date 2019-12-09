from random import randint

g = [1, 2]

player = False


while player == False:
    comp_move = g[randint(0, 1)]
    choice = input("Odd or Even")
    player = input("Do you choose 1 or 2?")
    move = int(player) + int(comp_move)

    print("I choose", comp_move)

    if choice == "Even":
        if move % 2 == 0:
            print("you win, the result is even")
        else:
            print("you lose, the result is odd")
    elif choice == "Odd":
        if move % 2 == 1:
            print("You Win! The result is odd")
        else:
            print("You lose, the result is even")
    print("the total is", move)

    player = False
