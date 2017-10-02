import SearchProblem
import GridGenerator
import SearchNode
import GenericSearch

class State():
    def __init__(self, x, y ,grid, max):
        self.x = x
        self.y = y
        self.grid = grid
        self.max = max


def run(gui):
        grid = GridGenerator.GenGrid()
        for x in range(len(grid)):
            for y in range(len(grid)):
                if grid[x][y] == 2:
                     initialState = State(x, y, grid, grid.max())

        operators = ['Up', 'Down', 'Left', 'Right']
        def goalTestFunction(state):
            print(state.max)
            return (state.max == 0)

        problem = SearchProblem.createSearchProblem(initialState, operators, goalTestFunction)

        result_node = GenericSearch.Search(problem, "DFS", True, gui);

        if result_node != None:
            path = []
            path.append(result_node.operator)
            parent = result_node.parent
            while parent != None:
                if parent.operator != None:
                    path.append(parent.operator)
                parent = parent.parent
            print("Solution", path)
        else:
            print("Found no solution")
# run(None)
