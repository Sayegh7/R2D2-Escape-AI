class StateSpaceNode(object):
    """docstring for State."""
    def __init__(self, x, y, grid, max):
        self.x = x;
        self.y = y;
        self.grid = grid;
        self.max = max;
        for operator in operators:
            self[operator] = nextState(self, operator)


def nextState(previousState, operator):
    newGrid = previousState.grid
    newX = previousState.x
    newY = previousState.y
    newMax = previousState.max
    if operator == "Up":
        # Check if at top edge
        if previousState.y > 0:
            # No obstacles in the way
            if (previousState.grid[previousState.x][previousState.y-1]) == 0:
                newGrid[previousState.x][previousState.y] == 0
                newY += 1
                newGrid[previousState.x][newY] == 0
                StateSpaceNode(newX, newY, newGrid, newMax)


def create(grid, initalState, operators):
    (x, y, grid, max) = initalState
    return StateSpaceNode(x, y, grid, max)
