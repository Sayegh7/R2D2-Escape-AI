import GridGenerator
import numpy as np
import math

def getDistance(p1, p2):
    return math.sqrt((p2[1]-p1[1])**2+(p2[0]-p1[0])**2)

def HeuristicOne(grid):
    print(grid)
    rocks = np.argwhere(grid==1)
    r2d2 = np.argwhere(grid==2)
    teleporter = np.argwhere(grid==-2)

    distances = []
    distanceSum = 0
    lastPosition = r2d2[0]
    for i in range(len(rocks)):
        for j in range(len(rocks)):
            distances.append(getDistance(lastPosition,rocks[j]))
        indexOfSmallestDistance = np.argmin(distances)
        lastPosition = rocks[indexOfSmallestDistance]
        distanceSum += distances[indexOfSmallestDistance]
        np.delete(rocks, indexOfSmallestDistance)
        distances = []

    distanceSum += getDistance(r2d2[0],teleporter[0])
    print(distanceSum)

grid = GridGenerator.GenGrid()
HeuristicOne(grid)
