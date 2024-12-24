from PIL import Image
import numpy as np

def get_brightness_matrix(pixel_matrix):
    brightness_matrix = np.zeros((pixel_matrix.shape[0], pixel_matrix.shape[1]))

    for i in range(len(pixel_matrix)):
        for j in range(len(pixel_matrix[i])):
            r, g, b = pixel_matrix[i][j]
            brightness_matrix[i][j] = 0.21*r + 0.72*g + 0.07*b

    return brightness_matrix

def brightness_to_ascii(ascii, brightness_matrix):
    ascii_matrix = np.empty(brightness_matrix.shape, dtype=str)

    for i in range(len(brightness_matrix)):
        for j in range(len(brightness_matrix[i])):
            index = int(brightness_matrix[i][j] / 255 * (len(ascii) - 1))
            ascii_matrix[i][j] = ascii[index]

    return ascii_matrix

def render_ascii(ascii_matrix):
    for row in ascii_matrix:
        for char in row:
            print(char, end="")
        print()

def main():
    ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    img = Image.open("geto.jpeg")

    px_arr = np.array(img)

    brightness_matrix = get_brightness_matrix(px_arr)
    ascii_matrix = brightness_to_ascii(ascii, brightness_matrix)
    render_ascii(ascii_matrix)

if __name__ == "__main__":
    main()
