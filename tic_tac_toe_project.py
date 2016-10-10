#Olivia Bicks ohb3fs

import random


# get the player choice and make sure that the input is valid
def get_human():
    choice = input("Please choose 'X' or 'O': ")
    while choice.lower() != "x" and choice.lower() != "o":
        choice = input("Sorry, that entry is invalid. Please choose 'X' or 'O': ")
    return choice.lower()


# get the move, make sure the number is valid and that the spot is empty
def get_human_move():
    spot = int(input("Choose a number between 1 and 9: ")) - 1
    while spot < 0 or spot > 8:
        spot = int(input("Sorry, that number is invalid. Choose a number between 1 and 9: ")) - 1
    while moves[spot] != " ":
        spot = int(input("Sorry, that square is already taken. Please pick a number between 1 and 9: ")) - 1
    return spot


# check if that move won the game
def check_winner():
    if moves[0] == moves[2] and moves[2] == moves[1] and moves[0] != " ":
        if moves[0] == human_player:
            return("You win!")
        elif moves[0] == computer_player:
            return("You lost!")
    elif moves[4] == moves[3] and moves[3] == moves[5] and moves[4] != " ":
        if moves[4] == human_player:
            return("You win!")
        elif moves[4] == computer_player:
            return ("You lose!")
    elif moves[6] == moves[7] and moves[7] == moves[8] and moves[7] != " ":
        if moves[6] == human_player:
            return ("You win!")
        elif moves[6] == computer_player:
            return("You lose!")
    elif moves[0] == moves[3] and moves[3] == moves[6] and moves[6] != " ":
        if moves[6] == human_player:
            return("You win!")
        elif moves[6] == computer_player:
            return ("You lose!")
    elif moves[1] == moves[4] and moves[4] == moves[7] and moves[1] != " ":
        if moves[1] == human_player:
            return ("You win!")
        elif moves[1] == computer_player:
            return("You lose!")
    elif moves[2] == moves[5] and moves[5] == moves[8] and moves[8] != " ":
        if moves[5] == human_player:
            return("You win!")
        elif moves[5] == computer_player:
            return ("You lose!")
    elif moves[0] == moves[4] and moves[4] == moves[8] and moves[0] != " ":
        if moves[0] == human_player:
            return("You win!")
        elif moves[0] == computer_player:
            return("You lose!")
    elif moves[2] == moves[4] and moves[4] == moves[6] and moves[2] != " ":
        if moves[2] == human_player:
            return("You win!")
        elif moves[2] == computer_player:
            return("You lose!")
    elif " " not in moves:
        return("Game over, no one wins!")
    else:
        return ("Keep playing")



#draws a 3 x 3 matrix with each move
def draw_board():
    print(" " + str(moves[0]) + " | " + str(moves[1]) + " | " + str(moves[2]))
    print(" " + str(moves[3]) + " | " + str(moves[4]) + " | " + str(moves[5]))
    print(" " + str(moves[6]) + " | " + str(moves[7]) + " | " + str(moves[8]))
    print("\n")

print("Let's Play Tic Tac Toe!")
human_player = get_human()
#see who goes first
turn = input("Who should go first? Choose p for player or c for computer: ")
# determine computer player
if human_player == "o":
    computer_player = 'x'
elif human_player == "x":
    computer_player = 'o'
moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
count = 0
while count >= 0:
    if turn == "p":
        if count % 2 == 0:
            move = get_human_move()
            moves[move] = human_player  # assigns human move to a spot on the matrix
            draw_board()
            check_winner()
            if check_winner() == "Keep playing":
                count += 1  # switch turns if no one has one
            else:
                print(check_winner())  # prints the winner and ends the game if player has won
                break
        elif count % 2 == 1:
            # determine computer winning move if possible
            if moves[0] == computer_player and moves[1] == computer_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[2] == computer_player and moves[1] == " ":
                moves[1] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == computer_player and moves[2] == computer_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == computer_player and moves[4] == computer_player and moves[5] == " ":
                moves[5] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == computer_player and moves[5] == computer_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[5] == computer_player and moves[4] == computer_player and moves[3] == " ":
                moves[3] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == computer_player and moves[7] == computer_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[7] == computer_player and moves[8] == computer_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == computer_player and moves[8] == computer_player and moves[7] == " ":
                moves[7] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[3] == computer_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[6] == computer_player and moves[3] == " ":
                moves[3] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == computer_player and moves[6] == computer_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == computer_player and moves[4] == computer_player and moves[7] == " ":
                moves[7] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == computer_player and moves[7] == computer_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[7] == computer_player and moves[4] == computer_player and moves[1] == " ":
                moves[1] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == computer_player and moves[5] == computer_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == computer_player and moves[8] == computer_player and moves[5] == " ":
                moves[5] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[5] == computer_player and moves[8] == computer_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[4] == computer_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[8] == computer_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[4] == computer_player and moves[8] == computer_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == computer_player and moves[4] == computer_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == computer_player and moves[4] == computer_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == computer_player and moves[2] == computer_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            # block player winning move if player can win
            elif moves[0] == human_player and moves[1] == human_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[2] == human_player and moves[1] == " ":
                moves[1] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == human_player and moves[2] == human_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == human_player and moves[4] == human_player and moves[5] == " ":
                moves[5] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == human_player and moves[5] == human_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[5] == human_player and moves[4] == human_player and moves[3] == " ":
                moves[3] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == human_player and moves[7] == human_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[7] == human_player and moves[8] == human_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == human_player and moves[8] == human_player and moves[7] == " ":
                moves[7] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[3] == human_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[6] == human_player and moves[3] == " ":
                moves[3] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == human_player and moves[6] == human_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == human_player and moves[4] == human_player and moves[7] == " ":
                moves[7] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == human_player and moves[7] == human_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[7] == human_player and moves[4] == human_player and moves[1] == " ":
                moves[1] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == human_player and moves[5] == human_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == human_player and moves[8] == human_player and moves[5] == " ":
                moves[5] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[5] == human_player and moves[8] == human_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[4] == human_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[8] == human_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[4] == human_player and moves[8] == human_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == human_player and moves[4] == human_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == human_player and moves[4] == human_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == human_player and moves[2] == human_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            # if computer nor player can win, choose a random spot for the computer move
            else:
                move = random.randint(0, 8)
                while moves[move] != " ":
                    move = random.randint(0,8)
                moves[move] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
    # changes the order if the computer goes first
    elif turn == "c":
        if count % 2 == 0:
            # computer chooses winning move if possible
            if moves[0] == computer_player and moves[1] == computer_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[2] == computer_player and moves[1] == " ":
                moves[1] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == computer_player and moves[2] == computer_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == computer_player and moves[4] == computer_player and moves[5] == " ":
                moves[5] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == computer_player and moves[5] == computer_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[5] == computer_player and moves[4] == computer_player and moves[3] == " ":
                moves[3] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == computer_player and moves[7] == computer_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[7] == computer_player and moves[8] == computer_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == computer_player and moves[8] == computer_player and moves[7] == " ":
                moves[7] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[3] == computer_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[6] == computer_player and moves[3] == " ":
                moves[3] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == computer_player and moves[6] == computer_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == computer_player and moves[4] == computer_player and moves[7] == " ":
                moves[7] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == computer_player and moves[7] == computer_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[7] == computer_player and moves[4] == computer_player and moves[1] == " ":
                moves[1] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == computer_player and moves[5] == computer_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == computer_player and moves[8] == computer_player and moves[5] == " ":
                moves[5] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[5] == computer_player and moves[8] == computer_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[4] == computer_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == computer_player and moves[8] == computer_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[4] == computer_player and moves[8] == computer_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == computer_player and moves[4] == computer_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == computer_player and moves[4] == computer_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == computer_player and moves[2] == computer_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            # blocks player's winning move
            elif moves[0] == human_player and moves[1] == human_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[2] == human_player and moves[1] == " ":
                moves[1] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == human_player and moves[2] == human_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == human_player and moves[4] == human_player and moves[5] == " ":
                moves[5] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == human_player and moves[5] == human_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[5] == human_player and moves[4] == human_player and moves[3] == " ":
                moves[3] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == human_player and moves[7] == human_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[7] == human_player and moves[8] == human_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == human_player and moves[8] == human_player and moves[7] == " ":
                moves[7] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[3] == human_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[6] == human_player and moves[3] == " ":
                moves[3] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[3] == human_player and moves[6] == human_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == human_player and moves[4] == human_player and moves[7] == " ":
                moves[7] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[1] == human_player and moves[7] == human_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[7] == human_player and moves[4] == human_player and moves[1] == " ":
                moves[1] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == human_player and moves[5] == human_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == human_player and moves[8] == human_player and moves[5] == " ":
                moves[5] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[5] == human_player and moves[8] == human_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[4] == human_player and moves[8] == " ":
                moves[8] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[0] == human_player and moves[8] == human_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[4] == human_player and moves[8] == human_player and moves[0] == " ":
                moves[0] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[2] == human_player and moves[4] == human_player and moves[6] == " ":
                moves[6] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == human_player and moves[4] == human_player and moves[2] == " ":
                moves[2] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            elif moves[6] == human_player and moves[2] == human_player and moves[4] == " ":
                moves[4] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
            else:
                move = random.randint(0, 8)
                while moves[move] != " ":
                    move = random.randint(0,8)
                moves[move] = computer_player
                draw_board()
                check_winner()
                if check_winner() == "Keep playing":
                    count += 1
                else:
                    print(check_winner())
                    break
        # if neither computer nor player can win, computer chooses random spot
        elif count % 2 == 1:
            move = get_human_move()
            moves[move] = human_player
            draw_board()
            check_winner()
            if check_winner() == "Keep playing":
                count += 1
            else:
                print(check_winner())
                break

