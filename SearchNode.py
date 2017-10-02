import GenericSearch
import numpy as np
class State():
    def __init__(self, x, y ,grid, max):
        self.x = x
        self.y = y
        self.grid = grid
        self.max = max

class SearchNode():
    def __init__(self, state, cost, depth, parent, operator):
        self.state = state
        self.cost = cost
        self.depth = depth
        self.parent = parent
        self.operator = operator
    def expand(self, operators):
        childNodes = []
        for operator in operators:
            newState = nextState(self.state, operator);
            newNode = SearchNode(self.state, self.cost+1, self.depth+1, self, operator)
            childNodes.append(newNode)
        return childNodes

def createNode(state, cost, depth, parent, operator):
    return SearchNode(state, cost, depth, parent, operator)

def nextState(previousState, operator):
    newGrid = np.copy(previousState.grid)
    gridCopy = np.copy(newGrid)
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
                    newGrid[previousState.x][previousState.y-1] = 0
                    newGrid[previousState.x][previousState.y] = 0
                    newY -= 1
                    return State(newX, newY, newGrid, 0)
                else:
                    # Not all pads are active. Do nothing.
                    return State(previousState.x, previousState.y, previousState.grid, previousState.max)

            # Pad in the way
            if (previousState.grid[previousState.x][previousState.y-1]) == -1 or (previousState.grid[previousState.x][previousState.y-1]) == -3:
                return State(previousState.x, previousState.y, previousState.grid, previousState.max)
            # No obstacles in the way
            if (previousState.grid[previousState.x][previousState.y-1]) == 0:
                # Move up
                newGrid[previousState.x][previousState.y] = 0
                newY -= 1
                newGrid[previousState.x][newY] = 2
                return State(newX, newY, newGrid, newMax)
            else:
                # Rock found
                # Check if rock is at the top
                if previousState.y == 1:
                    # Do nothing
                    return State(previousState.x, previousState.y, previousState.grid, previousState.max)
                else:
                    # Empty above rock
                    if (previousState.grid[previousState.x][previousState.y-2]) == 0:
                        # Move rock and self up
                        newGrid[previousState.x][previousState.y-2] = 1
                        newGrid[previousState.x][previousState.y-1] = 2
                        newGrid[previousState.x][previousState.y] = 0
                        newY -= 1
                        return State(newX, newY, newGrid, newMax)
                    # Rock or teleporter or full pad above rock
                    if (previousState.grid[previousState.x][previousState.y-2]) == 1 or (previousState.grid[previousState.x][previousState.y-2]) == -2 or (previousState.grid[previousState.x][previousState.y-2]) == -3 :
                        # Do nothing
                        return State(previousState.x, previousState.y, previousState.grid, previousState.max)
                    # Pad above rock
                    if (previousState.grid[previousState.x][previousState.y-2]) == -1:
                        # Move rock onto pad
                        newGrid[previousState.x][previousState.y-2] = -3
                        newGrid[previousState.x][previousState.y-1] = 2
                        newGrid[previousState.x][previousState.y] = 0
                        newY -= 1
                        return State(newX, newY, newGrid, newMax)
        # At Top edge
        else:
            # Do nothing
            return State(previousState.x, previousState.y, previousState.grid, previousState.max)



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
                    newGrid[previousState.x][previousState.y+1] = 0
                    newGrid[previousState.x][previousState.y] = 0
                    newY += 1
                    return State(newX, newY, newGrid, 0)
                else:
                    # Not all pads are active. Do nothing.
                    return State(previousState.x, previousState.y, previousState.grid, previousState.max)

            # Pad in the way
            if (previousState.grid[previousState.x][previousState.y+1]) == -1 or (previousState.grid[previousState.x][previousState.y+1]) == -3:
                return State(previousState.x, previousState.y, previousState.grid, previousState.max)
            # No obstacles in the way
            if (previousState.grid[previousState.x][previousState.y+1]) == 0:
                # Move up
                newGrid[previousState.x][previousState.y] = 0
                newY += 1
                newGrid[previousState.x][newY] = 2
                return State(newX, newY, newGrid, newMax)
            else:
                # Rock found
                # Check if rock is at the top
                if previousState.y == len(newGrid)-2:
                    # Do nothing
                    return State(previousState.x, previousState.y, previousState.grid, previousState.max)
                else:
                    # Empty above rock
                    if (previousState.grid[previousState.x][previousState.y+2]) == 0:
                        # Move rock and self up
                        newGrid[previousState.x][previousState.y+2] = 1
                        newGrid[previousState.x][previousState.y+1] = 2
                        newGrid[previousState.x][previousState.y] = 0
                        newY += 1
                        return State(newX, newY, newGrid, newMax)
                    # Rock or teleporter or full pad above rock
                    if (previousState.grid[previousState.x][previousState.y+2]) == 1 or (previousState.grid[previousState.x][previousState.y+2]) == -2 or (previousState.grid[previousState.x][previousState.y+2]) == -3 :
                        # Do nothing
                        return State(previousState.x, previousState.y, previousState.grid, previousState.max)
                    # Pad above rock
                    if (previousState.grid[previousState.x][previousState.y+2]) == -1:
                        # Move rock onto pad
                        newGrid[previousState.x][previousState.y+2] = -3
                        newGrid[previousState.x][previousState.y+1] = 2
                        newGrid[previousState.x][previousState.y] = 0
                        newY += 1
                        return State(newX, newY, newGrid, newMax)
        # At Top edge
        else:
            # Do nothing
            return State(previousState.x, previousState.y, previousState.grid, previousState.max)


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
                    newGrid[previousState.x+1][previousState.y] = 0
                    newGrid[previousState.x][previousState.y] = 0
                    newX += 1
                    return State(newX, newY, newGrid, 0)
                else:
                    # Not all pads are active. Do nothing.
                    return State(previousState.x, previousState.y, previousState.grid, previousState.max)

            # Pad in the way
            if (previousState.grid[previousState.x+1][previousState.y]) == -1 or (previousState.grid[previousState.x+1][previousState.y]) == -3:
                return State(previousState.x, previousState.y, previousState.grid, previousState.max)
            # No obstacles in the way
            if (previousState.grid[previousState.x+1][previousState.y]) == 0:
                # Move up
                newGrid[previousState.x][previousState.y] = 0
                newX += 1
                newGrid[newX][previousState.y] = 2
                return State(newX, newY, newGrid, newMax)
            else:
                # Rock found
                # Check if rock is at the top
                if previousState.x == len(newGrid)-2:
                    # Do nothing
                    return State(previousState.x, previousState.y, previousState.grid, previousState.max)
                else:
                    # Empty above rock
                    if (previousState.grid[previousState.x+2][previousState.y]) == 0:
                        # Move rock and self up
                        newGrid[previousState.x+2][previousState.y] = 1
                        newGrid[previousState.x+1][previousState.y] = 2
                        newGrid[previousState.x][previousState.y] = 0
                        newX += 1
                        return State(newX, newY, newGrid, newMax)
                    # Rock or teleporter or full pad above rock
                    if (previousState.grid[previousState.x+2][previousState.y]) == 1 or (previousState.grid[previousState.x+2][previousState.y]) == -2 or (previousState.grid[previousState.x+2][previousState.y]) == -3 :
                        # Do nothing
                        return State(previousState.x, previousState.y, previousState.grid, previousState.max)
                    # Pad above rock
                    if (previousState.grid[previousState.x+2][previousState.y]) == -1:
                        # Move rock onto pad
                        newGrid[previousState.x+2][previousState.y] = -3
                        newGrid[previousState.x+1][previousState.y] = 2
                        newGrid[previousState.x][previousState.y] = 0
                        newX += 1
                        return State(newX, newY, newGrid, newMax)
        # At Top edge
        else:
            # Do nothing
            return State(previousState.x, previousState.y, previousState.grid, previousState.max)





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
                    newGrid[previousState.x-1][previousState.y] = 0
                    newGrid[previousState.x][previousState.y] = 0
                    newX -= 1
                    return State(newX, newY, newGrid, 0)
                else:
                    # Not all pads are active. Do nothing.
                    return State(previousState.x, previousState.y, previousState.grid, previousState.max)

            # Pad in the way
            if (previousState.grid[previousState.x-1][previousState.y]) == -1 or (previousState.grid[previousState.x-1][previousState.y]) == -3:
                return State(previousState.x, previousState.y, previousState.grid, previousState.max)
            # No obstacles in the way
            if (previousState.grid[previousState.x-1][previousState.y]) == 0:
                # Move up
                newGrid[previousState.x][previousState.y] = 0
                newX -= 1
                newGrid[newX][previousState.y] = 2
                return State(newX, newY, newGrid, newMax)
            else:
                # Rock found
                # Check if rock is at the top
                if previousState.x == 1:
                    # Do nothing
                    return State(previousState.x, previousState.y, previousState.grid, previousState.max)
                else:
                    # Empty above rock
                    if (previousState.grid[previousState.x-2][previousState.y]) == 0:
                        # Move rock and self up
                        newGrid[previousState.x-2][previousState.y] = 1
                        newGrid[previousState.x-1][previousState.y] = 2
                        newGrid[previousState.x][previousState.y] = 0
                        newX -= 1
                        return State(newX, newY, newGrid, newMax)
                    # Rock or teleporter or full pad above rock
                    if (previousState.grid[previousState.x-2][previousState.y]) == 1 or (previousState.grid[previousState.x-2][previousState.y]) == -2 or (previousState.grid[previousState.x-2][previousState.y]) == -3 :
                        # Do nothing
                        return State(previousState.x, previousState.y, previousState.grid, previousState.max)
                    # Pad above rock
                    if (previousState.grid[previousState.x-2][previousState.y]) == -1:
                        # Move rock onto pad
                        newGrid[previousState.x-2][previousState.y] = -3
                        newGrid[previousState.x-1][previousState.y] = 2
                        newGrid[previousState.x][previousState.y] = 0
                        newX -= 1
                        return State(newX, newY, newGrid, newMax)
        # At Top edge
        else:
            # Do nothing
            return State(previousState.x, previousState.y, previousState.grid, previousState.max)
