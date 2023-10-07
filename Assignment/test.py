
class Sokoban:

    def __init__(self, board):
        self.board = board
        self.player = None
        self.crates = []
        self.score = 0
        self.moves = 0
        self.won = False
        self.height = len(board)
        self.width = len(board[0])
        self.player_x = None
        self.player_y = None
        self.crates_x = None
        self.crates_y = None
        self.find_player()


    def find_player(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == 'P':
                    self.player_x = col
                    self.player_y = row
                    self.player = self.board[row][col]
        return self.player_x, self.player_y

    def is_complete(self):
        return self.won

    def steps(self):
        return self.moves

    def restart(self):
        self.crates = []
        self.score = 0
        self.moves = 0
        self.won = False
        self.height = len(self.board)
        self.width = len(self.board[0])
        self.find_player()
        self.find_crates()

    def find_crates(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == '#':
                    self.crates_x = col
                    self.crates_y = row
                    self.crates.append(self.board[row][col])
        return self.crates_x, self.crates_y


    def undo(self):
        self.moves -= 1
        self.restart()
        return self.moves

    def move(self, direction):
        if direction == 'a':
            if self.player_x > 0:
                self.player_x -= 1
                self.moves += 1
                self.find_crates()
        elif direction == 's':
            if self.player_y > 0:
                self.player_y -= 1
                self.moves += 1
                self.find_crates()
        elif direction == 'w':
            if self.player_y < self.height - 1:
                self.player_y += 1
                self.moves += 1
                self.find_crates()
        elif direction == 'd':
            if self.player_x < self.width - 1:
                self.player_x += 1
                self.moves += 1
                self.find_crates()
    def __str__(self):
        result = ''
        for i in range(self.height):
            for j in range(self.width):
                result += str(self.board[i][j]) + ' '
            result += '\n'
        return result


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