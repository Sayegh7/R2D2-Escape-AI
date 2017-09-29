import SearchNode
import SearchProblem
import queue
import Visualizer as v
import numpy as np
def Search(problem, strategy, visualize, gui):
    global visitedMatrices
    global rockCount
    rockCount = 0
    visitedMatrices = []
    if strategy == "BFS":
        nodes = queue.Queue()
    (x,y,grid,max) = problem.initalState
    rootNode = SearchNode.createNode((x, y, grid, max), 0, 0, None, None)
    nodes.put(rootNode)
    while nodes.empty() == False:
        flag = False
        node = nodes.get()
        # print(node.state)
        # print (node.state[0],node.state[1])
        v.renderGrid(node.state[2], 5)
        gui.refresh()
        # if np.count_nonzero(y==1) != rockCount:
        #     visitedNodes = [] 
        gridArray = node.state[2]
        # print (grid)
        # print (node.state[0], node.state[1])
        if node.state[3] == 0: # GOAAAAAALLL
            return node
        childNodes = node.expand(problem.operators)
        # print (childNodes)
        for node in childNodes:
           for matrix in visitedMatrices:
               if np.array_equal(matrix,gridArray):
                        # print (matrix)
                        flag =True    
           if flag == False: 
                nodes.put(node)
        visitedMatrices.append(gridArray)
    return
