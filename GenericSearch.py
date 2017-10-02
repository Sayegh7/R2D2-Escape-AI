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
    visitedStates = []
    nodes = queue.Queue()
    '''
    rockCount = 0
    rockCount = np.count_nonzero(grid==1)
    '''
    rootNode = SearchNode.createNode(SearchNode.State(problem.initialState.x, problem.initialState.y, problem.initialState.grid, problem.initialState.max), 0, 0, None, None)
    nodes.put(rootNode)
    while nodes.empty() == False:
        newNodes =queue.Queue()
        flag = False
        node = nodes.get()
        if visualize == True:
            v.refresh(node.state, gui)
        '''
        if np.count_nonzero(node.state[2]==1) != rockCount:
            nodes = queue.Queue()
            rockCount = np.count_nonzero(node.state[2]==1)
            nodes.put(node)
            continue;
        '''
        if problem.goalTestFunction(node.state): #GOAL
            return node
        childNodes = node.expand(problem.operators)
        for node in childNodes:
            if (tracker.stateExist(node.state,visitedStates)==False):
                newNodes.put(node)
                visitedStates.append(node.state)
        Queueingfunction(newNodes,strategy)
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
