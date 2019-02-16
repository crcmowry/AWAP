"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
andrewid1
andrewid2
"""
import random
import graphsearch
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
        self.team_name = "Delta"
        self.companyval = [] #initialize and update


    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """
        actionName = {0:Direction.LEFT, 1:Direction.UP, 2:Direction.RIGHT, 3:Direction.DOWN, 4: Direction.REPLACE, 5:Direction.NONE}
        actions = []
        for i in range(self.team_size):
            search (self.costgrid, self.startpoint)
            for companies in self.company_info:


        return [Direction.UP, Direction.UP, Direction.UP, Direction.UP]
