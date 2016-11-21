## David Aldarondo 50177475
##OthelloGame
##
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
        self._move = position
        new_col = self._move[1]
        row = self._move[0]
        self.check_if_valid(row, new_col, True)
        if self._is_move_valid:
            self._board[row][new_col] = self._current_player[0]
            NUM.count()
        else:
            pass
##            self.turn(position)
        self._winner_ = self.check_win()
        if self._winner_:
            return('Done')
        else:
            pass
##            return self.turn(position)
        self.print_board()

    def check_win(self):
        '''In the top I tried to deal when there were no possible moves'''
##        for i in range(0, len(self._board)-1):
##            for x in range(0, len(self._board[0])):
##                self.check_if_valid(i, x, False)
##                if self._is_move_valid == True:
##                    return False
##                break        
##            else:
##                return True
##                else:
##                    if self._win_type == 'Most':
##                        if self._W > self._B:
##                            print('Winner is White!')
##                        elif self._W < self._B:
##                            print('Winner is Black!')
##                        elif self._W == self._B:
##                            print('Tie!')
##                    else:
##                        if self._W < self._B:
##                            print('Winner is White!')
##                        elif self._W > self._B:
##                            print('Winner is Black!')
##                        elif self._W == self._B:
##                            print('Tie!')
        self.count()
                        
        if self._W + self._B == self._rows * self._columns:
            if self._win_type == 'Most':
                if self._W > self._B:
                    self._win_text = 'Winner is White!'
                    print()
                elif self._W < self._B:
                    self._win_text = 'Winner is Black!'
                elif self._W == self._B:
                    self._win_text = 'Tie!'
            else:
                if self._W < self._B:
                    self._win_text = 'Winner is White!'
                elif self._W > self._B:
                    self._win_text = 'Winner is Black!'
                elif self._W == self._B:
                    self._win_text = 'Tie!'
        return self._W + self._B == self._rows * self._columns
    
    def check_s(self, row, new_col, flip):
        if self._board[row+1][new_col] == self._other_player[0]:#down S
            for i in range(row, len(self._board)-1):
                if self._board[i][new_col] == self._current_player[0]:
                    self._is_move_valid = True
                    self._end = [i,new_col]
                    if flip:
                        for m in range(row, self._end[0]):
                            for x in range(new_col, self._end[1]+1):
                                self._board[m][x] = self._current_player[0]
        else:
            pass

    def check_n(self, row, new_col, flip):
        if self._board[row-1][new_col] == self._other_player[0]:#up N
            for i in range(0, row):
                if self._board[i][new_col] == self._current_player[0]:
                    self._is_move_valid = True
                    self._end = [i, new_col]
                    if flip:
                        for m in range(self._end[0], row):
                            for x in range(new_col, self._end[1]+1):
                                self._board[m][x] = self._current_player[0]
        else:
            pass

    def check_e(self, row, new_col, flip):
        if self._board[row][new_col+1] == self._other_player[0]:#right E
            for i in range(new_col+1, len(self._board[0])):
                if self._board[row][i] == self._current_player[0]:
                    self._is_move_valid = True
                    self._end = [row, i]
                    if flip:
                        for m in range(int(row), self._end[0]+1):
                            for x in range(new_col, self._end[1]):
                                self._board[m][x] = self._current_player[0]
        else:
            pass

    def check_w(self, row, new_col, flip):
        if self._board[row][new_col-1] == self._other_player[0]:#left W
            for i in range(-(new_col), 0):
                if self._board[row][new_col + i] == self._current_player[0]:
                    self._is_move_valid = True
                    self._end = [row, new_col + i]
                    if flip:
                        for m in range(int(row), self._end[0]+1):
                            for x in range(self._end[1], new_col):
                                self._board[m][x] = self._current_player[0]

        else:
            pass
    def check_ne(self, row, new_col, flip):
        if self._board[row-1][new_col+1] == self._other_player[0]:
            if len(self._board)-1 <= len(self._board[0]):#if more columns than rows NE
                for i in range(1, len(self._board)-1):
                    if self._board[row-i][new_col+i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row-i,new_col + i]
                        print('True')
                        if flip:
                            for m in range(self._end[0]+1, row):
                                for x in range(new_col+1, self._end[1]):
                                    self._board[m][x] = self._current_player[0]
                        break
                    
            elif len(self._board) > len(self._board[0]):
                for i in range(1, len(self._board[0]) - new_col-1):
                    if self._board[row-i][new_col+i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row-i,new_col + i]
                        print('True')
                        if flip:
                            for m in range(int(self._end[0])+1, row):
                                for x in range(new_col+1, self._end[1]):
                                    self._board[m][x] = self._current_player[0]
                        break
            else:
                pass
                        
    def check_se(self, row, new_col, flip):
        if self._board[row+1][new_col+1] == self._other_player[0]: #SE
            if len(self._board)-1 <= len(self._board[0]): #if more columns than rows 
                for i in range(1, len(self._board)-1):
                    if self._board[row+i][new_col+i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row+i,new_col + i]
                        if flip:
                            for m in range(row, self._end[0]+1):
                                for x in range(new_col+1, self._end[1]):
                                    self._board[m][x] = self._current_player[0]
                        break

            elif len(self._board)-1 > len(self._board[0]): #if more rows
                for i in range(1, len(self._board[0])-1-new_col):
                    if self._board[row+i][new_col+i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row+i,new_col + i]
                        if flip:
                            for m in range(row, self._end[0]+1):
                                for x in range(new_col+1, self._end[1]):
                                    self._board[m][x] = self._current_player[0]
                        break
        else:
            pass
        
    def check_sw(self, row, new_col, flip):
        if self._board[row+1][new_col-1] == self._other_player[0]: #SW
            if len(self._board)-1 <= len(self._board[0]): #if more columns than rows
                for i in range(1, len(self._board)-1):
                    if self._board[row+i][new_col-i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row+i,new_col - i]
                        if flip:
                            for m in range(row+1, self._end[0]):
                                for x in reversed(range(self._end[1]+1, new_col)):
                                    self._board[m][x] = self._current_player[0]
                        break
                        
            elif len(self._board)-1 > len(self._board[0]): #if more rows than columns
                for i in range(1, len(self._board[0])):
                    if self._board[row+i][new_col-i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row+i,new_col - i]
                        if flip:
                            for m in range(row+1, self._end[0]):
                                for x in reversed(range(self._end[1]+1, new_col)):
                                    self._board[m][x] = self._current_player[0]
                        break
        else:
            pass

    def check_nw(self, row, new_col, flip):
        if self._board[row-1][new_col-1] == self._other_player[0]: #NW
            if len(self._board)-1 <= len(self._board[0]): #if more columns than rows
                for i in range(1, len(self._board)-1):
                    if self._board[row-i][new_col-i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row-i,new_col - i]
                        if flip:
                            for m in reversed(range(self._end[0]+1,row)):
                                for x in reversed(range(self._end[1]+1, new_col)):
                                    self._board[m][x] = self._current_player[0]
                        break
                                    
            elif len(self._board)-1 > len(self._board[0]): #if more rows than col
                for i in range(1, len(self._board[0]) - new_col-1):
                    if self._board[row-i][new_col-i] == self._current_player[0]:
                        self._is_move_valid = True
                        self._end = [row-i,new_col - i]
                        if flip:
                            for m in reversed(range(self._end[0]+1,row)):
                                for x in reversed(range(self._end[1]+1, new_col)):
                                    self._board[m][x] = self._current_player[0]
                        break
        else:
            pass

                
    def check_if_valid(self, row, new_col, flip):
        check_list = [self.check_n, self.check_s, self.check_e, self.check_w,
                      self.check_ne, self.check_nw, self.check_se, self.check_sw]
        self._is_move_valid = False
        if self._board[row][new_col] == ' ':
            for i in check_list:
                try:
                    i(row, new_col, flip)
                except:
                    pass
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
