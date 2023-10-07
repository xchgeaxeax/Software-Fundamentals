import copy
class Sokoban:

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

    def find_player(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == 'P':
                    return (i, j)
    def is_complete(self):
        for row in self.board:
            for cell in row:
                if cell == 'o':
                    return False
        return True
    def steps(self):
        return self.moves
    def find_crate(self):
        if self.crates is None:
            self.crates = []
            for i, row in enumerate(self.board):
                for j, cell in enumerate(row):
                    if cell == '#':
                        self.crates.append((i, j))
        return self.crates
    def restart(self):
        self.board = copy.deepcopy(self.original_board)
        self.moves = 0
        self.crates = None
        self.snapshots = []
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
    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.board])
    def get_crates(self):
        crates = []
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 2:
                    crates.append((x, y, self.crates[x][y]))
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
                self.board[self.new_position_crate[0]][self.new_position_crate[1]] = ' '
                return
            elif self.board[self.new_position_crate[0]][self.new_position_crate[1]] == ' ':
                self.board[self.new_position_crate[0]][self.new_position_crate[1]] = '#'
                return
        else:
            return
