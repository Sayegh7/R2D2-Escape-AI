import SearchNode
import SearchProblem
import queue
import Visualizer as v
import numpy as np
import tracking as tracker
def Search(problem, strategy, visualize, gui):
    global nodes
    global visitedStates
    global rockCount
    rockCount = 0
    visitedStates = []
    nodes = queue.Queue()
    (x,y,grid,max) = problem.initalState
    rockCount = np.count_nonzero(grid==1)

    rootNode = SearchNode.createNode((x, y, grid, max), 0, 0, None, None)
    nodes.put(rootNode)
    while nodes.empty() == False:
        newNodes =queue.Queue()
        flag = False
        node = nodes.get()
        v.renderGrid(node.state[2], 5)
        gui.refresh()
        gridArray = node.state[2]
        if np.count_nonzero(node.state[2]==1) != rockCount:
            nodes = queue.Queue()
            rockCount = np.count_nonzero(node.state[2]==1)
            nodes.put(node)
            continue;
        # visitedNodes.append((node.state[0], node.state[1], node.operator))
        if node.state[3] == 0: # GOAAAAAALLL
            return node
        childNodes = node.expand(problem.operators)
        # print (childNodes)
        for node in childNodes:
            if (tracker.stateExist(node.state,visitedStates)==False):
                newNodes.put(node)
                visitedStates.appand(node.state)
        visitedMatrices.append(gridArray)
        Queueingfucntion(newNodes,strategy)
    return

def Queueingfunction(newNodes,strategy):
    global nodes
    if strategy == "BFS":
        while not newNodes.empty():
            nodes.put(newNodes.get())
    if strategy == "DFS":
        while not nodes.empty():
            newNodes.put(nodes.get())
        while not newNodes.empty():
            nodes.put(newNodes.get())
