## David Aldarondo Othello
import OthelloGame

def rows_and_columns(m: str) -> int:
    try:
        x = int(input(m))
        if x >= 4 and x <= 16 and x%2 == 0:
            return x
    except:
        pass
    else:
        print('Invalid, Number must be an even integer between 4 and 16')
        return rows_and_columns(m)

def color_returner(m: str):
    try:
        x = str(input(m))
        if x[0] in 'Ww':
            return 'White'
        elif x[0] in 'Bb':
            return 'Black'
    except:
        pass
    else:
        print('Player is invalid, please type White or Black')
        return color_returner(m)

def how_to_win():
    try:
        x = str(input('How oes one win, with Most or Fewest pieces?: '))
        if x[0] in 'Mm':
            return 'Most'
        elif x[0] in 'Ff':
            return 'Fewest'
    except:
        pass
    else:
        print('Input is invalid, please type Most or Fewest')
        return how_to_win()




if __name__ == '__main__':
    x = OthelloGame.Gamestate()
    x.first_player(color_returner('Is the first player black or white?: '))
    x.top_left(color_returner('Which color is on the top left?: '))
    x.rows(rows_and_columns('Number of Rows: '))
    x.columns(rows_and_columns('Number of Columns: '))
    x.win_type(how_to_win())
    x.build_board()
    x.print_board()
    x.turn()

## Used to test out game
##
##    x = OthelloGame.Gamestate()
##    x.first_player('White')
##    x.top_left('White')
##    x.rows(8)
##    x.columns(8)
##    x.win_type('Most')
##    x.build_board()
##    x.print_board()
##    x.turn()





