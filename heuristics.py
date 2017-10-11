import GridGenerator
import numpy as np
import math

def getDistance(p1, p2):
    return math.sqrt((p2[1]-p1[1])**2+(p2[0]-p1[0])**2)
def getActualDistance(p1, p2):
    return math.fabs(p2[1]-p1[1])+math.fabs(p2[0]-p1[0])

def HeuristicOne(grid):
    # print(grid)
    rocks = np.argwhere(grid==1)
    r2d2 = np.argwhere(grid==2)
    teleporter = np.argwhere(grid==-2)
    if len(r2d2) == 0:
        return 0
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

    distanceSum += getDistance(lastPosition,teleporter[0])
    # print(distanceSum)
    return distanceSum
def HeuristicTwo(grid):
    # print(grid)
    rocks = np.argwhere(grid==1)
    r2d2 = np.argwhere(grid==2)
    teleporter = np.argwhere(grid==-2)
    if len(r2d2) == 0:
        return 0
    distances = []
    distanceSum = 0
    lastPosition = r2d2[0]
    for i in range(len(rocks)):
        for j in range(len(rocks)):
            distances.append(getActualDistance(lastPosition,rocks[j]))
        indexOfSmallestDistance = np.argmin(distances)
        lastPosition = rocks[indexOfSmallestDistance]
        distanceSum += distances[indexOfSmallestDistance]
        np.delete(rocks, indexOfSmallestDistance)
        distances = []

    distanceSum += getActualDistance(lastPosition,teleporter[0])
    # print(distanceSum)
    return distanceSum

# grid = GridGenerator.GenGrid()
# HeuristicTwo(grid)
