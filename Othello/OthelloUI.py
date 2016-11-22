##David Aldarondo 50177475
## OTHELLO UI
##When running the program, radiobutons will pop up, but sometimes they pop up
##Behind the python window
import tkinter
import OthelloGame



_BACKGROUND_COLOR = '#006400'

class Options:
    def __init__(self, s):
        """takes in a string to be used as a label for the radiobuttons"""
        self._text = s
        self._root = tkinter.Tk()

    def nums(self):
        """used for the rows and columns"""
        self._text = tkinter.Label(self._root, text = self._text)
        
        self._text.pack()

        
        self._var = tkinter.IntVar()

        self.MODES = [4, 6, 8, 10, 12, 14, 16]
        
        for num in self.MODES:
            b = tkinter.Radiobutton(self._root, text=str(num),
                            variable=self._var, value=num, command = self.sel)
            b.pack()

        self._root.mainloop()

    def colors(self):
        """Used for the top left and first player"""

        self._text = tkinter.Label(self._root, text = self._text)
        
        self._text.pack()

        
        self._var = tkinter.StringVar()

        self.MODES = ['Black', 'White']
        
        for color in self.MODES:
            b = tkinter.Radiobutton(self._root, text=color,
                            variable=self._var, value=color, command = self.sel)
            b.pack()

        self._root.mainloop()
    def win(self):
        """Used for win type"""

        self._text = tkinter.Label(self._root, text = self._text)
        
        self._text.pack()

        
        self._var = tkinter.StringVar()

        self.MODES = ['Most', 'Least']
        
        for color in self.MODES:
            b = tkinter.Radiobutton(self._root, text=color,
                            variable=self._var, value=color, command = self.sel)
            b.pack()

        self._root.mainloop()

    def sel(self):
        """sends the value to the a self attribute and then destroys the window"""
        self._x = self._var.get()
        self._quit()

    def get_num(self):
        """returns the chosen value/variable"""
        return self._x

    def _quit(self):
        """destroys the window"""
        self._root.destroy()




 

class OthelloApplication:
    def __init__(self, gamestate):
        """ Creates an application that takes a gamestate and uses it trought the class"""
        
        try: ##Incase the user decides to quit during the options input, the program will not crash
        
            r = Options('How many rows: ')
            r.nums()
            self._rows = r.get_num()
            c = Options('How many columns: ')
            c.nums()
            self._columns = c.get_num()
            f = Options('Which color goes first')
            f.colors()
            self._first = f.get_num()
            tl = Options('Which color is top left?')
            tl.colors()
            self._TopL = tl.get_num()
            w = Options('How do the players win?')
            w.win()
            self._win_type = w.get_num()

            x = gamestate() ## Creates a game in the application
            x.first_player(self._first)
            x.top_left(self._TopL)
            x.rows(self._rows)
            x.columns(self._columns)
            x.win_type(self._win_type)
            x.build_board()
            self.handle_turn(x)

            self._root_window = tkinter.Tk()

            self._othello_canvas = tkinter.Canvas(
                master = self._root_window, width = 500, height = 500,
                background = _BACKGROUND_COLOR)

            
            self._othello_canvas.grid(
                row = 2, column = 0, padx = 10, pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

            self._label = tkinter.Label(master = self._root_window, text = "Othello Game", font = ('Helvetica', 20))
            self._label.grid(row = 0, column = 0, sticky = tkinter.N)

            self._point_text = tkinter.StringVar()
            self._point_text.set('White: 2 Black: 2')
            self._label = tkinter.Label(master = self._root_window, textvariable = self._point_text, font = ('Helvetica', 20))
            self._label.grid(row = 1, column = 0, sticky = tkinter.N + tkinter.S)

            self._turn_text = tkinter.StringVar()
            self._turn_text.set('Turn: {}'.format(self._first))
            self._label = tkinter.Label(master = self._root_window, textvariable = self._turn_text, font = ('Helvetica', 20))
            self._label.grid(row = 3, column = 0, sticky = tkinter.N + tkinter.S)

            self._root_window.rowconfigure(0, weight = 0)
            self._root_window.rowconfigure(1, weight = 0)
            self._root_window.rowconfigure(2, weight = 1)
            self._root_window.rowconfigure(3, weight = 0)
            self._root_window.columnconfigure(0, weight = 1)
            
            self._othello_canvas.bind('<Button-1>', self._on_canvas_clicked)
            self._othello_canvas.bind('<Configure>', self._on_canvas_resized)
            
            self.create_lines(int(self._rows), int(self._columns))
            self.make_circles()



            self.start()
        except:
            pass
        else:
            pass
        

    def create_lines(self, r: int, c: int):
        """ Creates the lines on the canvas"""
        width = self._othello_canvas.winfo_width()
        height = self._othello_canvas.winfo_height()
        
        x = 0
        y = 0
        self.x_list = []
        self.y_list = []
        for i in range(0, r):
            self._othello_canvas.create_line(
                0, y, width, y,
                fill = '#000000')
            self.y_list.append(y)
            y+=(height/r)
        self.y_list.append(y)
        for i in range(0, c):
            self._othello_canvas.create_line(
                x, 0, x, height,
                fill = '#000000')
            self.x_list.append(x)
            x += (width/c)
        self.x_list.append(x)


    def make_circles(self):
        """Creates the Circles on the canvas"""
        width = self._othello_canvas.winfo_width()
        height = self._othello_canvas.winfo_height()
        
        for row in range(0, len(self._gamestate._board)):
            for col in range(0, len(self._gamestate._board[0])):
                if self._gamestate._board[row][col] == 'W':
                    self._othello_canvas.create_oval(self.x_list[col], self.y_list[row],
                                                     self.x_list[col+1], self.y_list[row+1],
                                                     fill = '#FFFFFF', outline = '#000000')
                elif self._gamestate._board[row][col] == 'B':
                    self._othello_canvas.create_oval(self.x_list[col], self.y_list[row],
                                                     self.x_list[col+1], self.y_list[row+1],
                                                     fill = '#000000', outline = '#000000')
                elif self._gamestate._board[row][col] == ' ':
                    pass


        



    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        """ What happens when canvas is clicked"""
        width = self._othello_canvas.winfo_width()
        height = self._othello_canvas.winfo_height()

        len_row = (height / self._rows)
        len_col = (width / self._columns)
        
        row = int(event.y/len_row)
        col = int(event.x/len_col)
        self.make_circles()
        self._position = [row, col]
        self._send(self._position)
        
        self._whites = self._gamestate._W
        self._blacks = self._gamestate._B
        self._point_text.set('White: {} Black: {}'.format(self._whites, self._blacks))

        
        self._turn_text.set('Turn: {}'.format(OthelloGame._check_player(self._first)))
        self.make_circles()
        if self._gamestate._winner_: ## Checks for a winner and replaces the turn Lable for a inner
            self._turn_text.set('Winner: {}'.format(self._gamestate._win_text))


    def _on_canvas_resized(self, event: tkinter.Event):
        """What happens if the window size is changed"""
        self._redraw_all()

    def _redraw_all(self) -> None:
        """Redraws the othello canvas"""


        self._othello_canvas.delete(tkinter.ALL)

        self.create_lines(int(self._rows), int(self._columns))
        self.make_circles()


        
    def _send(self, pos):
        self._turn(self._position)
        

    def start(self) -> None:
        self._root_window.mainloop()

    def handle_turn(self, gamestate):
        self._turn = gamestate.turn
        self._gamestate = gamestate


if __name__ == '__main__':
    # Create an OthelloApp and start it
    app = OthelloApplication(OthelloGame.Gamestate)

