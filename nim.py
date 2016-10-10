# Olivia Bicks ohb3fs


print("The Game of Nim \n")

total = int(input("Number of marbles are in the pile: "))
turn = input("Who will start? (p or c): ")
while total > 1:
    if turn == "p":
        print("The pile has", total, "marbles in it.")
        move = int(input("How many marbles do you want to take? (1-" + str(total//2) + "): "))
        while move > total // 2:
            move = int(input("How many marbles do you want to take? (1-" + str(total//2) + "): "))
        new_total = total - move
        total -= move
        turn = "c"
    elif turn == "c":
        print("The pile has", total, "marbles in it.")
        possibilities = []
        n = 1
        while ((2 ** n) - 1) <= total:
            possibilities.append((2 ** n) - 1)
            n += 1
        computer_moves = [1]
        for x in possibilities:
            potential_move = total - x
            if potential_move <= total // 2:
                computer_moves.append(potential_move)
        computer_move = max(computer_moves)
        print("The computer takes", computer_move, "marbles.")
        total -= computer_move
        turn = "p"
if total == 1 and turn == "p":
    print("The pile has 1 marbles in it.")
    input("How many marbles to do want to take? (1-1): ")
    print("The computer wins!")
elif total == 1 and turn == "c":
    print("The pile has 1 marbles in it.")
    print("The computer takes 1 marbles. \nThe player wins!")