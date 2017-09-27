import GridGenerator

class Grid(object):
    """docstring for Grid."""
    def __init__(self):
        self.grid = GridGenerator.GenGrid();
    def setGrid(self,grid):
        self.grid = grid
    def getGrid(self):
        return self.grid

def initGrid():
    return Grid()
