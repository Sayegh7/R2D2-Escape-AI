import SearchProblem
import GridGenerator
import SearchNode
import GenericSearch


def run(gui):
        grid = GridGenerator.GenGrid()
        problem = SearchProblem.createSearchProblem(grid)
        result_node = GenericSearch.Search(problem, "BFS", False, gui);
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
