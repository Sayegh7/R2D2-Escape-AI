import SearchNode
import SearchProblem
import queue
import Visualizer as v
import numpy as np
import tracking as tracker
import operator
def Search(problem, strategy, visualize, gui):
    global nodes
    global visitedStates
    visitedStates = []
    nodes = queue.Queue()
    rootNode = SearchNode.createNode(SearchNode.State(problem.initialState.x, problem.initialState.y, problem.initialState.grid, problem.initialState.max), 0, 0, None, None)
    nodes.put(rootNode)
    while nodes.empty() == False:
        newNodes =queue.Queue()
        flag = False
        node = nodes.get()
        if visualize == True:
            v.refresh(node.state, gui)
        if problem.goalTestFunction(node.state)or node.depth>max_depth: #GOAL
            return node
        childNodes = node.expand(problem.operators)
        for node in childNodes:
            print(tracker.stateExist(node.state,visitedStates))
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
    if strategy == "UC":
       templist = []
       while not nodes.empty():
           templist.append(nodes.get())
       while not newNodes.empty():
           templist.append(newNodes.get())
       templist.sort(key=operator.attrgetter('depth'))
       for node in templist:
           nodes.put(node)
