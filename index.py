import SearchProblem
import GridGenerator
import SearchNode
import GenericSearch


def run(gui):
    grid = GridGenerator.GenGrid()
    problem = SearchProblem.createSearchProblem(grid)
    result_node = GenericSearch.Search(problem, "BFS", False, gui);
    print (result_node)
