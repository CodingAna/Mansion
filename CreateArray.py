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

arrays = []

for y in range(img.height):
    temp = []
    for x in range(img.width):
        p = list(data[x, y])
        for i in range(3): p[i] = 0 if p[i] < 128 else 255
        p = tuple(p)
        temp.append(BLOCK_TYPES[p])
    arrays.append(temp)

lists = ""
for i in range(len(arrays)):
    lists += "{" + ",".join(x for x in arrays[i]) + "}->List " + str(i+1) + "\n"

print(lists)
