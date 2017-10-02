import numpy as np
def stateExist(state,visitedStates):
    for eachState in visitedStates:
        if np.array_equal(state.grid,eachState.grid):
                return True
    return False
