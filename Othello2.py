#Othello 2.0
## David Aldarondo OthelloGame

alpha = 'abcdefghijklmnop'

class Counter:
    def __init__(self):
        '''Initializes a Counter with a count of zero'''
        self._count = 0


    def count(self) -> int:
        '''Increments and returns the count'''
        self._count += 1
        return self._count


    def peek(self) -> int:
        '''Returns the count without updating it'''
        return self._count


    def reset(self) -> None:
        '''Resets the counter, so that its value is zero'''
        self._count = 0


NUM = Counter()
class Gamestate:
    def __init__(self):
        '''Starts up self'''
        self.__is_move_valid = False
##        self._board = None
##        self._first_player = None
##        self._top_left = None
##        self._rows = None
##        self._columns = None
##        self._win_type = None
##        self._move = None
##        self._is_move_valid = False
##        self._end = None

    def first_player(self, player):
        self._first_player = player

    def top_left(self, player):
        self._top_left = player
        
    def rows(self, num):
        self._rows = num
        
    def columns(self, num):
        self._columns = num
    def win_type(self, win):
        self._win_type = win
        
    def build_board(self) -> None:
        board = []
        col = []
        bottom = None
        for i in range(0, self._rows):
            board.append([])
            for x in range(0, self._columns):
                board[i].append(' ')
        if self._top_left == 'White':
            bottom = 'Black'
        else:
            bottom = 'White'
        board[int(self._rows/2)][int(self._columns/2)] = self._top_left[0]
        board[int(self._rows/2)-1][int(self._columns/2)-1] = self._top_left[0]
        board[int(self._rows/2)][int(self._columns/2)-1] = bottom[0]
        board[int(self._rows/2)-1][int(self._columns/2)] = bottom[0]
        for i in range(0,len(board[0])):
            col.append(alpha[i])
        board.append(col)
        self._board = board

    def print_board(self):
        print()
        y = len(self._board)
        for i in range(0, y-1):
            print('{:2d} {}'.format(i+1, self._board[i]))
        print(' C', self._board[y-1])
        self.count()
        print()
        print('White:', self._W)
        print('Black:', self._B)

    def turn(self):
        self._current_player = _check_player(self._first_player)
        if self._current_player == 'White':
            self._other_player = 'Black'
        else:
            self._other_player = 'White'
        print("TURN:", self._current_player)
        player_move = str(input('Please indicate Column and Row'))
        self._move = player_move.strip()
        if len(self._move) > 3:
            print('Please input Column and Row, ex. A1')
            turn(self, first_player)
        elif len(self._move) == 2 and self._move[0] in self._board[-1] and int(self._move[1]) <= len(self._board)-1:
            col = self._move[0]
            self._move_col = alpha.find(col.lower())
            self._move_row = int(self._move[1])-1
            self.check_if_valid()
            if self._is_move_valid:
                self._board[self._move_row][self._move_col] = self._current_player[0]
                NUM.count()
        elif len(self._move) == 3 and self._move[0] in self._board[-1] and int(self._move[1]) <= len(self._board)-1:
            col = self._move[0]
            self._move_col = alpha.find(col.lower())
            self._move_row = int(self._move[1:2])-1
            self.check_if_valid()
            if self._is_move_valid:
                self._board[self._move_row][self._move_col] = self._current_player[0]
                NUM.count()
        else:
            print('Please input Column and Row, ex. A1')
            turn(self, first_player)
        self.print_board()
        return self.turn()

    def check_if_valid(self):
        #self._is_move_valid = False
        check_list = [self.check_south, self.check_north, self.check_east, self.check_west, self.check_ne, self.check_se, self.check_sw, self.check_nw]
        if self._board[self._move_row][self._move_col] == ' ':
            for i in check_list:
                try:
                    i()
                except:
                    pass
                else:
                    pass

    def check_south(self):
        if self._board[self._move_row+1][self._move_col] == self._other_player[0]:#down S
                for i in range(self._move_row, len(self._board)-1):
                    if self._board[i][self._move_col] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [i,self._move_col]
                        for m in range(self._move_row, self._end[0]):
                            for x in range(self._move_col, self._end[1]+1):
                                self._board[m][x] = self._current_player[0]
                        pass
                    else:
                        pass
    def check_north(self):
        if self._board[self._move_row-1][self._move_col] == self._other_player[0]:#up N
            for i in range(0, self._move_row):
                if self._board[i][self._move_col] == self._current_player[0]:
                    self._is_move_valid = True
                    self._end = [i, self._move_col]
                    for m in range(self._end[0], self._move_row):
                        for x in range(self._move_col, self._end[1]+1):
                            self._board[m][x] = self._current_player[0]
                else:
                    pass
    def check_east(self):
        if self._board[self._move_row][self._move_col+1] == self._other_player[0]:#right E
            for i in range(self._move_col+1, len(self._board[0])):
                if self._board[self._move_row][i] == self._current_player[0]:
                    self._is_move_valid = True
                    self._end = [self._move_row, i]
                    for m in range(int(self._move_row), self._end[0]+1):
                        for x in range(self._move_col, self._end[1]):
                            self._board[m][x] = self._current_player[0]
    def check_west(self):
        if self._board[self._move_row][self._move_col-1] == self._other_player[0]:#left W
            for i in range(-(self._move_col), 0):
                if self._board[self._move_row][self._move_col + i] == self._current_player[0]:
                    self._is_move_valid = True
                    self._end = [self._move_row, self._move_col + i]
                    for m in range(int(self._move_row), self._end[0]+1):
                        for x in range(self._end[1], self._move_col):
                            self._board[m][x] = self._current_player[0]
                else:
                    pass
                
    def check_ne(self):
        if self._board[self._move_row-1][self._move_col+1] == self._other_player[0]:
            if len(self._board)-1 <= len(self._board[0]):#if more columns than rows NE
                for i in range(1, len(self._board) - self._move_col - 1):
                    if self._board[self._move_row-i][self._move_col+i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [self._move_row-i,self._move_col + i]
                        for m in range(int(self._end[0])+1, self._move_row):
                            for x in range(self._move_col+1, self._end[1]):
                                self._board[m][x] = self._current_player[0]
                    else:
                        pass
            elif len(self._board) > len(self._board[0]):
                        for i in range(1, len(self._board[0]) - self._move_col):
                            if self._board[self._move_row-i][self._move_col+i] == self._current_player[0]:
                                self._is_move_valid = True
                                self._end = [self._move_row-i,self._move_col + i]
                                for m in range(int(self._end[0])+1, self._move_row):
                                    for x in range(self._move_col+1, self._end[1]):
                                        self._board[m][x] = self._current_player[0]
                            else:
                                pass
    def check_se(self):
        if self._board[self._move_row+1][self._move_col+1] == self._other_player[0]: #SE
            if len(self._board)-1 <= len(self._board[0]): #if more columns than rows 
                for i in range(1, len(self._board)-1-self._move_col):
                    if self._board[self._move_row+i][self._move_col+i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [self._move_row+i,self._move_col + i]
                        for m in range(self._move_row+1, self._end[0]):
                            for x in range(self._move_col+1, self._end[1]):
                                self._board[m][x] = self._current_player[0]
                    else:
                        pass
            elif len(self._board)-1 > len(self._board[0]): #if the more columns than rows
                for i in range(1, len(self._board[0])-1-self._move_col):
                    #print(i)
                    if self._board[self._move_row+i][self._move_col+i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [self._move_row+i,self._move_col + i]
                        for m in range(self._move_row+1, self._end[0]):
                            for x in range(self._move_col+1, self._end[1]):
                                self._board[m][x] = self._current_player[0]
                    else:
                        pass
    def check_sw(self):
        if self._board[row+1][new_col-1] == self._other_player[0]: #SW
            print('true')
            if len(self._board)-1 <= len(self._board[0]): #if more columns than rows
                #print('more columns')
                for i in range(1, len(self._board)-1-row):
                    if self._board[row+i][new_col-i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row+i,new_col - i]
                        for m in range(self._move_row+1, self._end[0]):
                            for x in reversed(range(self._end[1]+1, self._move_col)):
                                print(x)
                                self._board[m][x] = self._current_player[0]
                    else:
                        pass
            elif len(self._board)-1 > len(self._board[0]): #if more rows than columns
                for i in range(1, len(self._board[0])-1-row):
                    if self._board[row+i][new_col-i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row+i,new_col - i]
                        for m in range(self._move_row+1, self._end[0]):
                            for x in reversed(range(self._end[1]+1, self._move_col-1)):
                                self._board[m][x] = self._current_player[0]
                    else:
                        pass


    def check_nw(self):
        if self._board[self._move_row-1][self._move_col-1] == self._other_player[0]: #NW
            if len(self._board)-1 <= len(self._board[0]): #if more columns than rows
                for i in reversed(range(1, len(self._board) - self._move_col)):
                    print(i)
                    if self._board[self._move_row-i][self._move_col-i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [self._move_row-i,self._move_col - i]
                        for m in range(self._end[0]+1,self._move_row):
                            print(m)
                            for x in reversed(range(self._end[1]+1, self._move_col)):
                                self._board[m][x] = self._current_player[0]
                    else:
                        pass
            elif len(self._board)-1 > len(self._board[0]): #if more rows than col
                for i in reversed(range(1, self._move_col+1)):
                    if self._board[self._move_row-i][self._move_col-i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [self._move_row-i,self._move_col - i]
                        for m in reversed(range(self._end[0]+1,self._move_row)):
                            for x in reversed(range(self._end[1]+1, self._move_col)):
                                self._board[m][x] = self._current_player[0]
                    else:
                        pass


                            
    def count(self):
        self._W = 0
        self._B = 0
        for i in self._board:
            for x in i:
                if x[0] == 'W':
                    self._W += 1
                elif x[0] == 'B':
                    self._B += 1

                    
def _check_player(first_player):
    if first_player == "White":
        second_player = "Black"
    else:
        second_player = "White"
    if NUM.peek() == 0:
        player = first_player
    elif NUM.peek() % 2 == 0:
        player = first_player
    elif NUM.peek() % 2 != 0:
        player = second_player
    return player
##def make_board_to_settings(board: 'board', x: str):
    


##def player_move


#print_board(build_board(6,8, 'White'))
