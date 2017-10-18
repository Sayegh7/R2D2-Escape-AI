import SearchProblem
import GridGenerator
import SearchNode
from State import State
import GenericSearch
import numpy as np
import heuristics
from termcolor import colored
from GUI import App
import sys
from PyQt5.QtWidgets import (QApplication)
GUIResults = {'BFS': [], 'DFS': [], 'UC': [], 'ID': [], 'A*': [], 'G': []}


# Parameters
# m refers to the size of the grid
m = 5
# Visualize flag
visualize = True
# Heuristic function choice
h = 1



def runGUI(results):
    app = QApplication(sys.argv)
    ex = App(results, m)
    sys.exit(app.exec_())

def output(result_node, strategy):
    if result_node != None:
        path = []
        states = []
        print_path = []
        states_path = []
        path.append(result_node.operator)
        parent = result_node.parent
        while parent != None:
            if parent.operator != None:
                path.append(parent.operator)
                states.append(parent.state.grid)
            parent = parent.parent
        print("Solution:")
        for value in reversed(path):
            print_path.append(value)
        print_path.append(result_node.operator)

        for value in reversed(states):
            GUIResults[strategy].append(value)
        GUIResults[strategy].append(result_node.state.grid)

        print (strategy, colored(print_path, 'yellow'))

    else:
        return

def run(visualize):
        print (colored("Thinking", 'red'))
        grid = GridGenerator.GenGrid(m)
        r2d2 = np.argwhere(grid==2)
        initialState = SearchNode.State(r2d2[0][0], r2d2[0][1], grid, grid.max())

        operators = ['Up', 'Down', 'Left', 'Right']
        def goalTestFunction(state):
            return (state.max == 0)

        def pathCostFunction(node):
            if h == 1:
                return heuristics.HeuristicOne(node.state.grid)
            elif h == 2:
                return heuristics.HeuristicTwo(node.state.grid)


        problem = SearchProblem.createSearchProblem(initialState, operators, goalTestFunction, pathCostFunction)
        for strategy in ["BFS", "DFS", "UC", "G", "A*"]:
            result_node = GenericSearch.Search(problem, strategy)
            output(result_node, strategy)
        for depth in range(99999999):
            GenericSearch.max_depth = depth
            result_node = GenericSearch.Search(problem, "ID")
            output(result_node, "ID")
            if result_node != None:
                print('the depth is ',depth)
                break
        if visualize == True:
            runGUI(GUIResults)
run(visualize)
sys.exit(0)
