import SearchNode
import SearchProblem
import Queue
import Visualizer as v
import numpy as np
import time
def Search(problem, strategy, visualize):
    global visitedNodes
    global rockCount
    rockCount = 0
    visitedNodes = []
    if strategy == "BFS":
        nodes = Queue.LifoQueue()
    (x,y,grid,max) = problem.initalState
    rootNode = SearchNode.createNode((x, y, grid, max), 0, 0, None, None)
    nodes.put(rootNode)
    while nodes.empty() == False:
        node = nodes.get()
        v.renderGrid(node.state[2], 10)
        time.sleep(1)
        if np.count_nonzero(y==1) != rockCount:
            visitedNodes = []
        visitedNodes.append((node.state[0], node.state[1], node.operator))
        print node.state[0], node.state[1]
        if node.state[3] == 0: # GOAAAAAALLL
            return node
        childNodes = node.expand(problem.operators)
        for node in childNodes:
             if not((node.state[0],node.state[1],node.operator) in visitedNodes) :
                nodes.put(node)
    return
