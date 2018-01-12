# global variables
ALPHA = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
BLACK_CHESS = "●"
WHITE_CHESS = "○"

# constants defined here are for evaluations
# variables begins with S means single
SONE = 1
STWO = 3
STHREE = 6
SFOUR = 7
# variables only with numbers means open
ONE = 2
TWO = 4
THREE = 7
FOUR = 50
FIVE = 100
# variables begins with D means double
DTWO = 5
DTHREE = 15
DFOUR = 75
# variables begins with DEF means defence
DEFTWO = 6
DEFTHREE = 30
DEFDTHREE = 40


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

    def available_point(self):
        '''
        Find all the available points within the bounded area, and stored in a dictionary
        :return: {point: 0} where point is a str
        '''
        moves = {}
        # initialize four bounds for available area
        up = 0
        down = 0
        left = 0
        right = 0
        # loop through self._board to find the up and left bounds
        i = 1
        while i < 16:
            # initialize left_not_found
            left_not_found = True
            j = 1
            # loop through each element in nest lest
            while left_not_found and j < 16:
                # if curr has something then record it
                if self._board[i][j] != "-":
                    left_not_found = False
                    # if left has not been found or this j is better then change j
                    if left == 0 or left > j:
                        left = j - 1 if j > 1 else 1
            # the first time we found one chess is up bound
            if up == 0 and not left_not_found:
                up = i - 1 if i > 1 else 1

        # use the same way to calculate down and right bound
        # by initialize i = 15, j = 15, and then count down
        i = 15
        while i > 0:
            right_not_found = True
            j = 15
            while right_not_found and j > 0:
                if self._board[i][i] != "-":
                    right_not_found = False
                    if right == 0 or right < j:
                        right = j + 1 if j < 15 else 15
            if down == 0 and right_not_found:
                down = i + 1 if i < 15 else 15

        # for the bound area, find all the available points
        for i in range(up, down + 1):
            for j in range(left, right + 1):
                if self._board[i][j] == "-":
                    moves[chr(j + 96) + str(i)] = 0
        return moves

    def evaluate(self):
        '''
        Evaluate all the available points and so the moves dict will become
        {point: value} where point is a str and value is a int.
        And then flip the dict, so keys will be int, and values will be list of str
        :return: {value: [point]} where value is int, point is str
        '''
        moves = self.avaiable_point()
        # get all the points
        points = moves.keys()
        # loop through each point
        # TODO evaluate each point in two sides:
        # TODO if you can win
        # TODO if you can stop the other win




        flip_moves = {}
        # loop each pairs in moves
        for key in moves.keys():
            if moves[key] in flip_moves:
                flip_moves[moves[key]].append(key)
            else:
                flip_moves[moves[key]] = [key]
        return flip_moves

    def AI_next_move(self):
        '''
        The function will return the first point in the highest value's list.
        :return: str
        '''
        moves = self.evaluate()
        points = moves.keys()
        points.sort()
        return moves[points[-1]][0] if self._board[8][8]!= "-" else "h8"
