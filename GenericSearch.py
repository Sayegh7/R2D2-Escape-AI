import SearchProblem
import queue
import Visualizer as v
import numpy as np
import tracking as tracker
import operator
from State import State
from SearchNode import SearchNode

max_depth = 9999999
def Search(problem, strategy, visualize, gui=None):
    global nodes
    global visitedStates
    visitedStates = []
    nodes = queue.Queue()
    rootNode = SearchNode(problem.initialState, 0, 0, None, None)
    nodes.put(rootNode)
    while nodes.empty() == False:
        newNodes =queue.Queue()
        node = nodes.get()
        if visualize == True:
            v.refresh(node.state, gui)
        if problem.goalTestFunction(node.state):#GOAL
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
    global max_depth
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
    if strategy == "ID":
                  while not nodes.empty():
                      newNodes.put(nodes.get())
                  while not newNodes.empty():
                      tempNode = newNodes.get()
                      if tempNode.depth<=max_depth:
                          nodes.put(tempNode)
