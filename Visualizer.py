from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5 import QtCore
# from PIL.ImageQt import ImageQt


def renderCell(img, x, y, background):
    img_w, img_h = img.size
    bg_w, bg_h = background.size
    offset = (50*x, 50*y)
    background.paste(img, offset)

def refresh(state, gui):
    renderGrid(state.grid, dimension)
    gui.refresh()

def renderGrid(grid, m, initial=False):
    global dimension
    dimension = m
    background = Image.new('RGBA', (m*50, m*50), (255, 255, 255, 255))
    emptyCellImg = Image.open('assets/box.png', 'r')
    rockImg = Image.open('assets/rock.png', 'r')
    r2d2Img = Image.open('assets/r2d2.jpg', 'r')
    padImg = Image.open('assets/pad.png', 'r')
    fullpadImg = Image.open('assets/fullpad.png', 'r')
    teleporterImg = Image.open('assets/teleporter.png', 'r')
    immovableImg = Image.open('assets/immovable.png', 'r')

    for x in range(m):
        for y in range(m):
            if grid[x][y] == -1:
                renderCell(padImg, x, y, background)
            if grid[x][y] == 1:
                renderCell(rockImg, x, y, background)
            if grid[x][y] == 2:
                renderCell(r2d2Img, x, y, background)
            if grid[x][y] == -2:
                renderCell(teleporterImg, x, y, background)
            if grid[x][y] == -3:
                renderCell(fullpadImg, x, y, background)
            if grid[x][y] == 0:
                renderCell(emptyCellImg, x, y, background)
            if grid[x][y] == -4:
                renderCell(immovableImg, x, y, background)
    if initial == True:
        background.save('initial.png')
        background.show()

    background.save('out.png')


def toQImage(im, copy=False):
    if im is None:
        return QImage()

    if im.dtype == np.uint8:
        if len(im.shape) == 2:
            qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
            qim.setColorTable(gray_color_table)
            return qim.copy() if copy else qim

        elif len(im.shape) == 3:
            if im.shape[2] == 3:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888);
                return qim.copy() if copy else qim
            elif im.shape[2] == 4:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32);
                return qim.copy() if copy else qim

    raise NotImplementedException
