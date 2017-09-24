from PIL import Image


def renderCell(img, x, y, background):
    img_w, img_h = img.size
    bg_w, bg_h = background.size
    offset = (50*x, 50*y)
    background.paste(img, offset)

def renderGrid(grid, m):
    background = Image.new('RGBA', (m*50, m*50), (255, 255, 255, 255))
    emptyCellImg = Image.open('assets/box.png', 'r')
    rockImg = Image.open('assets/rock.png', 'r')
    r2d2Img = Image.open('assets/r2d2.jpg', 'r')
    padImg = Image.open('assets/pad.jpeg', 'r')
    teleporterImg = Image.open('assets/teleporter.png', 'r')

    for x in range(m):
        for y in range(m):
            if grid[x][y] == -1:
                renderCell(padImg, x, y, background)
            if grid[x][y] == 1:
                renderCell(rockImg, x, y, background)
            if grid[x][y] == 2:
                renderCell(r2d2Img, x, y, background)
                print 'R2D2 is at', x, y
            if grid[x][y] == -2:
                renderCell(teleporterImg, x, y, background)
            if grid[x][y] == 0:
                renderCell(emptyCellImg, x, y, background)
    background.save('assets/out.png')
    background.show()
