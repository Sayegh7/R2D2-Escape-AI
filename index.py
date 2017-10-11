import SearchProblem
import GridGenerator
import SearchNode
from State import State
import GenericSearch

def run(gui):
        grid = GridGenerator.GenGrid()
        for x in range(len(grid)):
            for y in range(len(grid)):
                if grid[x][y] == 2:
                     initialState = SearchNode.State(x, y, grid, grid.max())

        operators = ['Up', 'Down', 'Left', 'Right']
        def goalTestFunction(state):
            return (state.max == 0)

        problem = SearchProblem.createSearchProblem(initialState, operators, goalTestFunction)
        result_node = GenericSearch.Search(problem, "BFS", True, gui=gui)

        # for depth in range(99999999):
        #     print ('the actual depth',depth)
        #     GenericSearch.max_depth = depth
        #     print(GenericSearch.max_depth)
        #     result_node = GenericSearch.Search(problem, "ID", True, gui=gui)
        #     if result_node != None:
        #         print('the depth is ',depth)
        #         break

        if result_node != None:
            path = []
            print_path = []
            path.append(result_node.operator)
            parent = result_node.parent
            while parent != None:
                if parent.operator != None:
                    path.append(parent.operator)
                parent = parent.parent
            print("Solution:")
            for value in reversed(path):
                print_path.append(value)
            print (print_path)
        else:
            print("Found no solution")
