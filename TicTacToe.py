# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
# import calendar
# import datetime


# TIC - TAC - TOE

# board
# show board
# play game
# handle turn - valid input or not
# check for win
    # check rows
    # check col
    # check diagonals
# check for tie
# flip player


board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

game_still_going = True


def make_move(player_turn):
    # this function will first of all take the position
    pos = int(input("Choose a position from (1-9) > ")) - 1
    # by sub 1 we will get the correct index
    if board[pos] == "_":
        # firstly check if the position which user ask for in invalid
        # for that case we have to ask him to try again
        # now what we have to do is to assign the value at that place
        board[pos] = player_turn
    # the game will start from X
    # after getting input we have to show board
        show_board()
    else:
        print("The position you entered in invalid!!")
        print("It seams that position is not empty!!")
        make_move(player_turn)


def show_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():

    # now if you want to play the game the first you need to do is to display the board
    show_board()

    # now after showing board we have to use a loop until the game finish
    # as we don't know the final range we will use while loop
    # now after showing the board we ned to ask user for input

    current_player = "X"
# we have been defined game still going to be global variable
    # let say if the function check_game_over says that game ends then we will assign game_still_going to be false
    while game_still_going:
        # while the game is not finish make move
        make_move(current_player)

        # now check if game over or not
        if check_game_over() == "Tie":
            print("Game Draw")
            break
        elif check_game_over():
            print("Game Ends and player", current_player, "wins!")
            break
        # now change the turn
        current_player = flip_player(current_player)


def check_game_over():
    # we have to check if all the positions are filled or not
    # if yes then check if some player wins or tie

    if check_wins():
        return True
    elif check_tie():
        return "Tie"
    else:
        return False


def check_wins():
    # we have to check if any player wins
    # for that we have to check rows
    # check col
    # check diagonals
    if check_row() or check_col() or check_dia():
        return True
    else:
        return False


def check_row():
    if (board[0] == board[1] == board[2] == "X" or board[3] == board[4] == board[5] == "X" or board[6] == board[7] == board[8] == "X") or (board[0] == board[1] == board[2] == "O" or board[3] == board[4] == board[5] == "O" or board[6] == board[7] == board[8] == "O"):
        return True
    else:
        return False


def check_col():
    if (board[0] == board[3] == board[6] == "X" or board[1] == board[3+1] == board[6+1] == "X" or board[0+2] == board[3+2] == board[6+2] == "X") or (board[0] == board[3] == board[6] == "O" or board[1] == board[3+1] == board[6+1] == "O" or board[0+2] == board[3+2] == board[6+2] == "O"):
        return True
    else:
        return False


def check_dia():
    if (board[0] == board[4] == board[8] == "X" or board[2] == board[4] == board[6] == "X" ) or (board[0] == board[4] == board[8] == "O" or board[2] == board[4] == board[6] == "O" ):
        return True
    else:
        return False


def flip_player(current):
    # it will just turn X to O
    if current == "X":
        return "O"
    else:
        return "X"


def check_tie():
    # we have to check if game tie
    # we will check this after checking win

    # not we will check if this game is tie or not

    if "_" not in board and not check_wins():
        return "Tie"
    else:
        return False


play_game()
