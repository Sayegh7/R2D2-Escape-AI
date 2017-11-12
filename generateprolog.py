import numpy as np
# import Visualizer as v

# ROCKS = 1, PADS = -1, R2D2 = 2, TELEPORTER = -2, FULL PAD = -3, IMMOVABLE = -4
m = 0
grid = []
def GenGrid(size):
    global m
    m = size
    global grid
    grid = np.zeros((size, size))
    file = open('knowledgebase.pl','w')
    file.write('% \n')
    file.close()
    rocks = np.random.randint(round(size/2))
    for n in range(rocks):
        placeRock()
        placePad()
    for n in range(round(rocks/2)):
        placeImmovable()
    placeTeleporter()
    placeR2D2()
    file = open('knowledgebase.pl','a')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j]==0):
                string2 = 'cell('+str(i)+','+str(j)+','+'s'+').'
                file.write(string2+'\n')
    file.close()

    # v.renderGrid(grid, size, True)
    return grid


def placeRock():
    placeItem(1)
def placePad():
    placeItem(-1)
def placeImmovable():
    placeItem(-4)
def placeTeleporter():
    placeItem(-2)
def placeR2D2():
    placeItem(2)

def placeItem(itemCode):
    while True:
        x = np.random.randint(m-1)
        y = np.random.randint(m-1)
        if y == 0 or y == m-1 or x == 0 or x == m-1:
            continue
        if grid[x][y] != 0:
            continue
        file = open('knowledgebase.pl','a')
        if (itemCode==1):
            predicit = 'rock('+str(x)+','+str(y)+','+'s'+').'+'\n'
        if (itemCode==-1):
            predicit = 'pad('+str(x)+','+str(y)+','+'s'+').'+'\n'
        if (itemCode==-4):
            predicit = 'immovable('+str(x)+','+str(y)+','+'s'+').'+'\n'
        if (itemCode==-2):
            predicit = 'teleporter('+str(x)+','+str(y)+','+'s'+').'+'\n'
        if (itemCode==2):
            predicit = 'r2d2('+str(x)+','+str(y)+','+'s'+').'+'\n'
        file.write(predicit)
        file.close()
        if grid[x][y] == 0:
            grid[x][y] = itemCode
            return
GenGrid(10)
