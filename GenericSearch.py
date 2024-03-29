import SearchProblem
import queue
import Visualizer as v
import numpy as np
import tracking as tracker
import operator
from State import State
from SearchNode import SearchNode

max_depth = 9999999
def Search(problem, strategy):
    global nodes
    global visitedStates
    visitedStates = []
    nodes = queue.Queue()
    rootNode = SearchNode(problem.initialState, 0, 0, None, None)
    nodes.put(rootNode)
    while nodes.empty() == False:
        newNodes =queue.Queue()
        node = nodes.get()
        if problem.goalTestFunction(node.state):#GOAL
            return node
        childNodes = node.expand(problem.operators)
        for node in childNodes:
            if (tracker.stateExist(node.state,visitedStates)==False):
                newNodes.put(node)
                visitedStates.append(node.state)
        Queueingfunction(newNodes,strategy, problem)
    return
def Queueingfunction(newNodes,strategy, problem):
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
    if strategy == "G":
        costs = []
        nodeList = []
        while not nodes.empty():
            one_node = nodes.get()
            nodeList.append(one_node)
        while not newNodes.empty():
            one_node = newNodes.get()
            nodeList.append(one_node)
        for nodeInArray in nodeList:
            costs.append(problem.pathCostFunction(nodeInArray))
        order = np.argsort(costs)
        ordered_nodes = []
        for index in range(len(order)):
            ordered_nodes.insert(order[index], nodeList[index])
        for node in ordered_nodes:
            nodes.put(node)
    if strategy == "A*":
        costs = []
        nodeList = []
        while not nodes.empty():
            one_node = nodes.get()
            nodeList.append(one_node)
        while not newNodes.empty():
            one_node = newNodes.get()
            nodeList.append(one_node)
        for nodeInArray in nodeList:
            costs.append(problem.pathCostFunction(nodeInArray)+nodeInArray.cost)
        order = np.argsort(costs)
        ordered_nodes = []
        for index in range(len(order)):
            ordered_nodes.insert(order[index], nodeList[index])
        for node in ordered_nodes:
            nodes.put(node)
