import numpy as np
import TransitionFunction
from State import State

class SearchNode():
    def __init__(self, state, cost, depth, parent, operator):
        self.state = state
        self.cost = cost
        self.depth = depth
        self.parent = parent
        self.operator = operator
    def expand(self, operators):
        childNodes = []
        for operator in operators:
            newState = nextState(self.state, operator);
            newNode = SearchNode(newState, self.cost+1, self.depth+1, self, operator)
            childNodes.append(newNode)
        return childNodes
def nextState(state, operator):
    return TransitionFunction.next(state, operator)

def createNode(state, cost, depth, parent, operator):
    return SearchNode(state, cost, depth, parent, operator)
