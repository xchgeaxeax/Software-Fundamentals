class Sokoban:
"""Creates a Sokoban instance with a given board
parameter. The board parameter is a nested list
containing the characters of the starting board."""
    def __init__(self, board):
        self.board = board
        self.player = None
        self.boxes = []
        self.goals = []
        self.moves = []
        self.moves_made = 0
        self.moves_possible = 0
        self.is_solved = False
        self.is_lost = False
        self.is_won = False
        self.is_valid = True
        self.is_finished = False
        self.is_moving = False
        self.is_moving_box = False
        self.is_moving_player = False
