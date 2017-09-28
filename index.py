import SearchProblem
import GridGenerator
import SearchNode
import GenericSearch


def run(gui):
    while True:
        grid = GridGenerator.GenGrid()
        problem = SearchProblem.createSearchProblem(grid)
        result_node = GenericSearch.Search(problem, "BFS", False, gui);
        print(result_node)
        if result_node != None:
            path = []
            print('here')
            move = 'nothing'
            while move != None:
                print(move)
                move = result_node.operator
                path.append(move)
            print(path)
        else:
            continue
