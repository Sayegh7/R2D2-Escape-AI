class SearchNode():
    def __init__(self, state, cost, depth, parent, operator):
        self.state = state
        self.cost = cost
        self.depth = depth
        self.parent = parent
        self.operator = operator
        return

def createNode(state):
    return SearchNode(state, cost, depth, parent, operator)
