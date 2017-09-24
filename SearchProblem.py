import numpy as np
import StateSpace
class SearchProblem():
    """docstring for SearchProblem."""
    def __init__(self, grid):
        """The search problem is as follows:
            Initial state: (x, y, grid, max) where x and y are R2D2's coordinates, grid is the current grid and max is the maximum value of the grid
            Operators: (up, down, left, right) directions in which R2D2 can move
            State space: All the possible states of the problem
            Goal test function: If the max = 0, this is a goal state
            Path cost function: Cost is the number of steps R2D2 has taken
        """
        self.grid = grid
        self.initalState = self.createInitialState()
        self.operators = ['Up', 'Down', 'Left', 'Right']
        self.stateSpace =   self.createStateSpace()
    def createInitialState(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                if self.grid[x][y] == 2:
                    return (x, y, self.grid, self.grid.max())
    def createStateSpace(self):
        return StateSpace.create(self.grid, self.initalState, self.operators)


    def goalTestFunction(self, state):
        state.gridsum == 0

def createSearchProblem(grid):
    return SearchProblem(grid)
