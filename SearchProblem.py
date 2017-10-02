import numpy as np
import StateSpace
class SearchProblem():
    """docstring for SearchProblem."""
    def __init__(self, initialState, operators, goalTestFunction):
        """The search problem is as follows:
            Initial state: (x, y, grid, max) where x and y are R2D2's coordinates, grid is the current grid and max is the maximum value of the grid
            Operators: (up, down, left, right) directions in which R2D2 can move
            State space: All the possible states of the problem
            Goal test function: If the max = 0, this is a goal state
            Path cost function: Cost is the number of steps R2D2 has taken
        """
        self.initialState = initialState
        self.operators = operators
        self.goalTestFunction = goalTestFunction

def createSearchProblem(initialState, operators, goalTestFunction):
    return SearchProblem(initialState, operators, goalTestFunction)
