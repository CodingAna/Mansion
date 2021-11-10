from PIL import Image

img = Image.open("Level.png")
data = img.load()

BLOCK_TYPES = {
    (  0,  0,  0): "0",
    (  0,  0,255): "1",
    (  0,255,  0): "2",
    (  0,255,255): "3",
    (255,  0,  0): "4",
    (255,  0,255): "5",
    (255,255,  0): "6",
    (255,255,255): "7",
}

"""
#Invert image
for y in range(img.height):
    for x in range(img.width):
        p = data[x, y]
        data[x, y] = tuple([255 - p[i] for i in range(3)])
"""

"""
For Y Chunk:
    For X Chunk:
        temp = []
        For Y Pixel:
            For X Pixel:
                p = clamped(pixel(xChunk*21+xPixel, yChunk*7+yPixel))
                block = BLOCK_TYPES[p]
                temp.append(block)
        array.append(temp)
"""
xChunk, yChunk = 1, 1
xPixel, yPixel = 21, 7
floor = []
for yc in range(yChunk):
    for xc in range(xChunk):
        for yp in range(yPixel):
            for xp in range(xPixel):
                p = list(data[xc*21+xp, yc*7+yp])
                for i in range(3): p[i] = 0 if p[i] < 128 else 255
                p = tuple(p)
                block = BLOCK_TYPES[p]
                floor.append(block)

# TODO: Export chunk limits too. (1->E, 2->F)

f = "{" + ",".join(t for t in floor) + "}->List 1"
print(f)
