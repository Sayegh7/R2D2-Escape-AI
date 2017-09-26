import SearchProblem
import GridGenerator
import SearchNode
import GenericSearch

grid = GridGenerator.GenGrid()
problem = SearchProblem.createSearchProblem(grid)
print GenericSearch.Search(problem, "BFS", False);
