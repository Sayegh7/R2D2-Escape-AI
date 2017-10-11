import SearchProblem
import GridGenerator
import SearchNode
from State import State
import GenericSearch
import numpy as np
import heuristics
from termcolor import colored

def output(result_node, strategy):
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
        print (strategy, colored(print_path, 'blue'))
    else:
        return

def run(gui):
        grid = GridGenerator.GenGrid()
        r2d2 = np.argwhere(grid==2)
        initialState = SearchNode.State(r2d2[0][0], r2d2[0][1], grid, grid.max())

        operators = ['Up', 'Down', 'Left', 'Right']
        def goalTestFunction(state):
            return (state.max == 0)

        def pathCostFunction(node):
            return heuristics.HeuristicOne(node.state.grid)

        problem = SearchProblem.createSearchProblem(initialState, operators, goalTestFunction, pathCostFunction)
        for strategy in ["BFS", "DFS", "UC", "G", "A*"]:
            result_node = GenericSearch.Search(problem, strategy, True, gui=gui)
            output(result_node, strategy)
        for depth in range(99999999):
            GenericSearch.max_depth = depth
            result_node = GenericSearch.Search(problem, "ID", True, gui=gui)
            output(result_node, "ID")
            if result_node != None:
                print('the depth is ',depth)
                break
