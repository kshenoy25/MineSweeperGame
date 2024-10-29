import random
# create a board object to represent the minesweeper game
# " create new board object " or " dig here " or " render this game for this object "
class Board:
    def __init__(self, dim_size, num_bombs):
        # keep track of the parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # board creation
        self.board = self.make_new_board() # plant the bombs

        # initialize a set to keep track of which locations have not been covered
        # save (row, col) tuples into this set
        self.dug = set() # dig at 0.0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dimension size and num of bombs
        # construct a list of lists
        # there is a 2-D board, list of lists is most natural

        # generate new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # creates an array:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]

        # representation of the board

        # plant the bombs
        bombs_planted = 0
        while bombs_planted > self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # returns a random integer N such that a <= N <= b
            row = loc // self.dim_size # want the number of times dim_size goes into loc
            col = loc % self.dim_size # want the remainder to find the column index

            if board[row][col] == '*':
                # means bomb was planted there already so keep going
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board



# play the game
def play(dim_size = 10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, display game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #          next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig --> VICTORy!
    pass

