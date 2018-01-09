from board import *


def main():
    '''
    Main function is using to start the game.
    :return: None
    '''
    # create the board
    board = Board()
    # ask for players' name and set names
    name1 = input("Please enter the first player's name: ")
    name2 = input("Please enter the second player's name: ")
    board.set_name_1(name1)
    board.set_name_2(name2)
    # show the board
    print(board)
    finish = False
    # loop until the game ends
    while not finish:
        # get the next move
        move = input()
        # get the move until it is valid
        while not valid_move(move) or board.already_have(move):
            move = input("Please enter a valid move: ")
        # and move to board and get the result
        (player, is_finish) = board.next_move(move)
        # show the new board
        print(board)
        # if finished to check if anyone won or tie
        if is_finish:
            # show if anyone won or there is a tie
            if isinstance(player, str):
                print(player, "won!")
            else:
                print("It is a tie.")
            # ask for play again
            order = input("Do you want to play again? (y, n, s) : ")
            # ask for valid order
            while order not in ['y', 'n', 's']:
                order = input("if you want to play again, enter 'y'\n"
                              "if you want to switch players, enter 's'\n"
                              "if you want to leave the game, enter 'n'\n"
                              "Do you want to play again? (y, n, s) : ")
            # play again and clear the board
            if order == 'y':
                board.clear()
                print(board)
            # end the game
            elif order == 'n':
                finish = True
                print("GAME OVER!")
            # switch players' names and play again
            else:
                board.clear()
                board.switch()
                print(board)


if __name__ == "__main__":
    main()
