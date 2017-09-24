class StateSpaceNode(object):
    """docstring for State."""
    def __init__(self, x, y, grid, max):
        self.x = x;
        self.y = y;
        self.grid = grid;
        self.max = max;
# ROCKS = 1, PADS = -1, R2D2 = 2, TELEPORTER = -2, FULL PAD = -3
    def expand(self):
        childNodes = []
        for operator in operators:
            childNodes.append(nextState(self, operator))
        return childNodes
def newNode(x, y, grid, max):
    return StateSpaceNode(x,y,grid,max)

def nextState(previousState, operator):
    newGrid = previousState.grid
    gridCopy = newGrid
    newX = previousState.x
    newY = previousState.y
    newMax = previousState.max


    if operator == "Up":
        # If not at top edge
        if previousState.y > 0:
            # Teleporter in the way
            if (previousState.grid[previousState.x][previousState.y-1]) == -2:
                gridCopy[previousState.x][previousState.y] = 0
                maxWithoutR2 = gridCopy.max()
                # All pads are active
                if maxWithoutR2 == 0:
                    # Success
                    newGrid[previousState.x][previousState.y-1] == 0
                    newGrid[previousState.x][previousState.y] == 0
                    newY -= 1
                    return newNode(newX, newY, newGrid, 0)
                else:
                    # Not all pads are active. Do nothing.
                    return previousState

            # Pad in the way
            if (previousState.grid[previousState.x][previousState.y-1]) == -1 or (previousState.grid[previousState.x][previousState.y-1]) == -3:
                return previousState
            # No obstacles in the way
            if (previousState.grid[previousState.x][previousState.y-1]) == 0:
                # Move up
                newGrid[previousState.x][previousState.y] == 0
                newY -= 1
                newGrid[previousState.x][newY] == 2
                return newNode(newX, newY, newGrid, newMax)
            else:
                # Rock found
                # Check if rock is at the top
                if previousState.y == 1:
                    # Do nothing
                    return previousState
                else:
                    # Empty above rock
                    if (previousState.grid[previousState.x][previousState.y-2]) == 0:
                        # Move rock and self up
                        newGrid[previousState.x][previousState.y-2] == 1
                        newGrid[previousState.x][previousState.y-1] == 2
                        newGrid[previousState.x][previousState.y] == 0
                        newY -= 1
                        return newNode(newX, newY, newGrid, newMax)
                    # Rock or teleporter or full pad above rock
                    if (previousState.grid[previousState.x][previousState.y-2]) == 1 or (previousState.grid[previousState.x][previousState.y-2]) == -2 or (previousState.grid[previousState.x][previousState.y-2]) == -3 :
                        # Do nothing
                        return previousState
                    # Pad above rock
                    if (previousState.grid[previousState.x][previousState.y-2]) == -1:
                        # Move rock onto pad
                        newGrid[previousState.x][previousState.y-2] == -3
                        newGrid[previousState.x][previousState.y-1] == 2
                        newGrid[previousState.x][previousState.y] == 0
                        newY -= 1
                        return newNode(newX, newY, newGrid, newMax)
        # At Top edge
        else:
            # Do nothing
            return previousState



    if operator == "Down":
        # If not at top edge
        if previousState.y < len(newGrid)-1:
            # Teleporter in the way
            if (previousState.grid[previousState.x][previousState.y+1]) == -2:
                gridCopy[previousState.x][previousState.y] = 0
                maxWithoutR2 = gridCopy.max()
                # All pads are active
                if maxWithoutR2 == 0:
                    # Success
                    newGrid[previousState.x][previousState.y+1] == 0
                    newGrid[previousState.x][previousState.y] == 0
                    newY += 1
                    return newNode(newX, newY, newGrid, 0)
                else:
                    # Not all pads are active. Do nothing.
                    return previousState

            # Pad in the way
            if (previousState.grid[previousState.x][previousState.y+1]) == -1 or (previousState.grid[previousState.x][previousState.y+1]) == -3:
                return previousState
            # No obstacles in the way
            if (previousState.grid[previousState.x][previousState.y+1]) == 0:
                # Move up
                newGrid[previousState.x][previousState.y] == 0
                newY += 1
                newGrid[previousState.x][newY] == 2
                return newNode(newX, newY, newGrid, newMax)
            else:
                # Rock found
                # Check if rock is at the top
                if previousState.y == len(newGrid)-2:
                    # Do nothing
                    return previousState
                else:
                    # Empty above rock
                    if (previousState.grid[previousState.x][previousState.y+2]) == 0:
                        # Move rock and self up
                        newGrid[previousState.x][previousState.y+2] == 1
                        newGrid[previousState.x][previousState.y+1] == 2
                        newGrid[previousState.x][previousState.y] == 0
                        newY += 1
                        return newNode(newX, newY, newGrid, newMax)
                    # Rock or teleporter or full pad above rock
                    if (previousState.grid[previousState.x][previousState.y+2]) == 1 or (previousState.grid[previousState.x][previousState.y+2]) == -2 or (previousState.grid[previousState.x][previousState.y+2]) == -3 :
                        # Do nothing
                        return previousState
                    # Pad above rock
                    if (previousState.grid[previousState.x][previousState.y+2]) == -1:
                        # Move rock onto pad
                        newGrid[previousState.x][previousState.y+2] == -3
                        newGrid[previousState.x][previousState.y+1] == 2
                        newGrid[previousState.x][previousState.y] == 0
                        newY += 1
                        return newNode(newX, newY, newGrid, newMax)
        # At Top edge
        else:
            # Do nothing
            return previousState


    if operator == "Right":
        # If not at top edge
        if previousState.x < len(newGrid)-1:
            # Teleporter in the way
            if (previousState.grid[previousState.x+1][previousState.y]) == -2:
                gridCopy[previousState.x][previousState.y] = 0
                maxWithoutR2 = gridCopy.max()
                # All pads are active
                if maxWithoutR2 == 0:
                    # Success
                    newGrid[previousState.x+1][previousState.y] == 0
                    newGrid[previousState.x][previousState.y] == 0
                    newX += 1
                    return newNode(newX, newY, newGrid, 0)
                else:
                    # Not all pads are active. Do nothing.
                    return previousState

            # Pad in the way
            if (previousState.grid[previousState.x+1][previousState.y]) == -1 or (previousState.grid[previousState.x+1][previousState.y]) == -3:
                return previousState
            # No obstacles in the way
            if (previousState.grid[previousState.x+1][previousState.y]) == 0:
                # Move up
                newGrid[previousState.x][previousState.y] == 0
                newX += 1
                newGrid[previousState.x][newX] == 2
                return newNode(newX, newY, newGrid, newMax)
            else:
                # Rock found
                # Check if rock is at the top
                if previousState.x == len(newGrid)-2:
                    # Do nothing
                    return previousState
                else:
                    # Empty above rock
                    if (previousState.grid[previousState.x+2][previousState.y]) == 0:
                        # Move rock and self up
                        newGrid[previousState.x+2][previousState.y] == 1
                        newGrid[previousState.x+1][previousState.y] == 2
                        newGrid[previousState.x][previousState.y] == 0
                        newX += 1
                        return newNode(newX, newY, newGrid, newMax)
                    # Rock or teleporter or full pad above rock
                    if (previousState.grid[previousState.x+2][previousState.y]) == 1 or (previousState.grid[previousState.x+2][previousState.y]) == -2 or (previousState.grid[previousState.x+2][previousState.y]) == -3 :
                        # Do nothing
                        return previousState
                    # Pad above rock
                    if (previousState.grid[previousState.x+2][previousState.y]) == -1:
                        # Move rock onto pad
                        newGrid[previousState.x+2][previousState.y] == -3
                        newGrid[previousState.x+1][previousState.y] == 2
                        newGrid[previousState.x][previousState.y] == 0
                        newX += 1
                        return newNode(newX, newY, newGrid, newMax)
        # At Top edge
        else:
            # Do nothing
            return previousState





    if operator == "Left":
        # If not at top edge
        if previousState.x > 0:
            # Teleporter in the way
            if (previousState.grid[previousState.x-1][previousState.y]) == -2:
                gridCopy[previousState.x][previousState.y] = 0
                maxWithoutR2 = gridCopy.max()
                # All pads are active
                if maxWithoutR2 == 0:
                    # Success
                    newGrid[previousState.x-1][previousState.y] == 0
                    newGrid[previousState.x][previousState.y] == 0
                    newX -= 1
                    return newNode(newX, newY, newGrid, 0)
                else:
                    # Not all pads are active. Do nothing.
                    return previousState

            # Pad in the way
            if (previousState.grid[previousState.x-1][previousState.y]) == -1 or (previousState.grid[previousState.x-1][previousState.y]) == -3:
                return previousState
            # No obstacles in the way
            if (previousState.grid[previousState.x-1][previousState.y]) == 0:
                # Move up
                newGrid[previousState.x][previousState.y] == 0
                newX -= 1
                newGrid[previousState.x][newX] == 2
                return newNode(newX, newY, newGrid, newMax)
            else:
                # Rock found
                # Check if rock is at the top
                if previousState.x == 1:
                    # Do nothing
                    return previousState
                else:
                    # Empty above rock
                    if (previousState.grid[previousState.x-2][previousState.y]) == 0:
                        # Move rock and self up
                        newGrid[previousState.x-2][previousState.y] == 1
                        newGrid[previousState.x-1][previousState.y] == 2
                        newGrid[previousState.x][previousState.y] == 0
                        newX -= 1
                        return newNode(newX, newY, newGrid, newMax)
                    # Rock or teleporter or full pad above rock
                    if (previousState.grid[previousState.x-2][previousState.y]) == 1 or (previousState.grid[previousState.x-2][previousState.y]) == -2 or (previousState.grid[previousState.x-2][previousState.y]) == -3 :
                        # Do nothing
                        return previousState
                    # Pad above rock
                    if (previousState.grid[previousState.x-2][previousState.y]) == -1:
                        # Move rock onto pad
                        newGrid[previousState.x-2][previousState.y] == -3
                        newGrid[previousState.x-1][previousState.y] == 2
                        newGrid[previousState.x][previousState.y] == 0
                        newX -= 1
                        return newNode(newX, newY, newGrid, newMax)
        # At Top edge
        else:
            # Do nothing
            return previousState
def create(grid, initalState, operatorsList):
    (x, y, grid, max) = initalState
    global operators
    operators = operatorsList
    global memoizedStates
    memoizedStates = []
    global memoizedNodes
    memoizedNodes = []

    return newNode(x, y, grid, max)
