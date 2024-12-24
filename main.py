from PIL import Image

img=Image.open("geto.jpeg")
px=img.load()
(width,height)=img.size

pixel_matrix=[[0 for _ in range(height)] for _ in range(width)]

for x in range(width):
    for y in range(height):
        pixel_matrix[x][y]=(px[x,y])
#print(pixel_matrix)

brightness_matrix=[(r+g+b)/3 for row in pixel_matrix for (r,g,b) in row]
print(brightness_matrix)

# test
