# global variables
ALPHA = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
BLACK_CHESS = "●"
WHITE_CHESS = "○"


class Board:
    '''
    The class represents a board for the game.
    '''

    def __init__(self):
        '''
        The function Initialize two players and the board.
        '''
        self._player_name_1 = ""
        self._player_name_2 = ""
        self._is_1_turn = True
        self._board = [["\\", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
                       ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["11", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["12", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["13", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["14", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["15", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]

    def set_name_1(self, name):
        self._player_name_1 = name

    def set_name_2(self, name):
        self._player_name_2 = name

    def __str__(self):
        '''
        Get the str representation of the board.
        :return: the str represents the board
        '''
        # initialize the str as result
        str = ''
        # loop through each row
        row_num = 0
        for row in self._board:
            # loop through each each column in each row
            column_num = 0
            for column in row:
                # for number 1-9, add two whitespace
                if row_num <= 9 and column_num == 0:
                    str = str + column + "  "
                # for others, add onw whitespace
                else:
                    str = str + column + " "
                column_num += 1
            str += "\n"
            row_num += 1
        # add players' names and chess signs
        str = str + self._player_name_1 + " " + BLACK_CHESS + "   " + self._player_name_2 + " " + WHITE_CHESS
        return str

    def already_have(self, move):
        return True if self._board[int(move[1:len(move)])][ord(move[0])-96] != "-" else False

    def who_wins(self, move):
        '''
        Check if one player won or if there is a tie.
        Check if curr move have same signs in four directions.
        :param move: curr move
        :return: a tuple of curr player and if he/she won, if there is a tie, return None and True
        '''
        # get player's name of current player
        player = self._player_name_1 if self._is_1_turn else self._player_name_2
        # get the check sign for chess
        if self._is_1_turn:
            check = BLACK_CHESS
        else:
            check = WHITE_CHESS

        # check row directions
        # initialize count, i, and j
        count = 1
        i = int(move[1:len(move)])
        j = ord(move[0]) - 96
        # first check left direction
        j -= 1
        while 0 < j and self._board[i][j] == check:
            count += 1
            j -= 1
        # let j go back to initial position
        j = ord(move[0]) - 96
        # then check right direction
        j += 1
        while j < len(self._board) and self._board[i][j] == check:
            count += 1
            j += 1
        # if count is greater or equal to 5, then return True
        if count >= 5:
            return (player, True)

        # check column direction
        # initialize count, i, and j
        count = 1
        i = int(move[1:len(move)])
        j = ord(move[0]) - 96
        # first check upper direction
        i -= 1
        while 0 < i and self._board[i][j] == check:
            count += 1
            i -= 1
        # let i go back to initial position
        i = int(move[1:len(move)])
        # then check down direction
        i += 1
        while i < len(self._board[0]) and self._board[i][j] == check:
            count += 1
            i += 1
        # if count is greater or equal to 5, then return True
        if count >= 5:
            return (player, True)

        # left up to right down
        # initialize count, i, and j
        count = 1
        i = int(move[1:len(move)])
        j = ord(move[0]) - 96
        # first check left up direction
        i -= 1
        j -= 1
        while 0 < i and 0 < j and self._board[i][j] == check:
            count += 1
            i -= 1
            j -= 1
        # let i, and j go back to initial position
        i = int(move[1:len(move)])
        j = ord(move[0]) - 96
        # then check right down direction
        i += 1
        j += 1
        while i < len(self._board[0]) and j < len(self._board) and self._board[i][j] == check:
            count += 1
            i += 1
            j += 1
        # if count is greater than or equal to 5, then return True
        if count >= 5:
            return (player, True)

        # right up to left down
        # initialize count, i, and j
        count = 1
        i = int(move[1:len(move)])
        j = ord(move[0]) - 96
        # first check right up direction
        i -= 1
        j += 1
        while 0 < i and j < len(self._board) and self._board[i][j] == check:
            count += 1
            i -= 1
            j += 1
        # let i, and j go back to initial position
        i = int(move[1:len(move)])
        j = ord(move[0]) - 96
        # then check left down direction
        i += 1
        j -= 1
        while i < len(self._board[0]) and 0 < j and self._board[i][j] == check:
            count += 1
            i += 1
            j -= 1
        # if count is greater than or equal to 5, then return True
        if count >= 5:
            return (player, True)

        # check for there is no space to move
        total_board = []
        for row in self._board:
            total_board += row
        return (player, False) if "-" in total_board else (None, True)

    def next_move(self, move):
        '''
        Add the curr move to the board.
        :param move: curr move
        :return: a tuple by method who_wins()
        '''
        # add curr move to board with signs
        if self._is_1_turn:
            self._board[int(move[1:len(move)])][ord(move[0])-96] = BLACK_CHESS
        else:
            self._board[int(move[1:len(move)])][ord(move[0])-96] = WHITE_CHESS
        (player, is_finished) = self.who_wins(move)
        # change another player to move
        self._is_1_turn = not self._is_1_turn
        return (player, is_finished)

    def clear(self):
        '''
        Clear the board.
        :return: None
        '''
        self._is_1_turn = True
        self._board = [["\\", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
                       ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["11", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["12", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["13", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["14", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                       ["15", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]

    def switch(self):
        '''
        Switch two players' names.
        :return: None
        '''
        self._player_name_1, self._player_name_2 = self._player_name_2, self._player_name_1


def valid_move(move):
    '''
    Check if input move is valid.
    :param move: a str represents move
    :return: boolean
    '''
    if isinstance(move, str) and len(move) <= 3 and move[0] in ALPHA and move[1:len(move)] in NUM:
        result = True
    else:
        result = False
    return result
