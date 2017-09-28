import numpy as np
import Visualizer as v

m = 5
grid = np.zeros((m, m))
# ROCKS = 1, PADS = -1, R2D2 = 2, TELEPORTER = -2, FULL PAD = -3

def GenGrid():
    rocks = 2#np.random.randint(m)
    for n in range(rocks):
        placeRock()
        placePad()
    placeTeleporter()
    placeR2D2()
    v.renderGrid(grid, m)
    return grid

def placeRock():
    placeItem(1)
def placePad():
    placeItem(-1)
def placeTeleporter():
    placeItem(-2)
def placeR2D2():
    placeItem(2)

def placeItem(itemCode):
    placed = False
    while placed == False:
        x = np.random.randint(m-1)
        y = np.random.randint(m-1)
        if y == 0 or y == m-1 or x == 0 or x == m-1:
            continue
        if grid[x][y] != 0:
            continue
        else:
            grid[x][y] = itemCode
            placed = True
