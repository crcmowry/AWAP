"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
cmowry
bpek
"""
from awap2019 import Tile, Direction, State


class Team(object):
    def __init__(self, initial_board, team_size, company_info):
        """
        The initializer is for you to precompute anything from the
        initial board and the company information! Feel free to create any
        new instance variables to help you out.

        Specific information about initial_board and company_info are
        on the wiki. team_size, although passed to you as a parameter, will
        always be 4.
        """
        self.board = initial_board
        self.team_size = team_size
        self.company_info = company_info

        self.team_name = "TODO: Change this"  # Add your team name here!

        self.scores = [company_info]*4
        self.intentions = [None]*4

        y = len(self.board)
        x = len(self.board[0])
        area = x * y


        # Computes a 2d array of the costs. Entry i,j corresponds with the cost
        # to enter tile i,j. It is set to TODO if the tile is a booth.
        self.costs = [[0 for tile in row] for row in self.board]
        for i in range(y):
            for j in range(x):
                tile = self.board[i][j]
                company = tile.get_booth()
                if (not company is None):
                    # We can't go here!
                    self.costs[i][j] = 1000000      # arbitrary large constant
                elif (not tile.get_line() is None):
                    self.costs[i][j] = 5
                else:
                    self.costs[i][j] = 3
        print(self.costs)


        # Computes the line lengths for each company.
        total_score = 0
        for v in self.company_info.values():
            total_score += v
        self.line_lengths = {k: (v * area)/(2 * total_score)
                             for (k, v) in self.company_info.items()}


        # line_locations is a map mapping companies to the start of their line
        # and the end of their line
        self.line_locations = {k: {"start": (None, None), "end": (None, None)}
                               for (k, v) in self.company_info.items()}
        def find_end(i, j):
            company = self.board[i][j].get_line()
            if (i > 0 and self.board[i-1][j].get_line() == company):
                while (i > 0 and self.board[i-1][j].get_line() == company):
                    i -= 1
                return (i, j)
            if (y > i and self.board[i+1][j].get_line() == company):
                while (y > i and self.board[i+1][j].get_line() == company):
                    i += 1
                return (i, j)
            if (j > 0 and self.board[i][j-1].get_line() == company):
                while (j > 0 and self.board[i][j-1].get_line() == company):
                    j -= 1
                return (i, j)
            if (x > j and self.board[i][j+1].get_line() == company):
                while (x > j and self.board[i][j+1].get_line() == company):
                    j += 1
                return (i, j)

        for i in range(y):
            for j in range(x):
                tile = self.board[i][j]
                if (tile.is_end_of_line()):
                    self.line_locations[tile.get_line()]["start"] = (i, j)
                    self.line_locations[tile.get_line()]["end"] = find_end(i, j)

        print(self.line_locations)

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """

        return [Direction.UP]*4
