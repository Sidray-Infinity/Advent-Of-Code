
import numpy as np
import matplotlib.pyplot as plt


def num_zeros(layer):
    count = 0
    for l in layer:
        if l == 0:
            count += 1

    return count


def num_ones(layer):
    count = 0
    for l in layer:
        if l == 1:
            count += 1

    return count


def num_twos(layer):
    count = 0
    for l in layer:
        if l == 2:
            count += 1

    return count


def decode_image(image):
    """
    * Returns a WIDTH * HEIGTH decoded image
    * image.shape = (100, 6, 25)
    """

    res = []

    for i in range(6):
        row = []
        for j in range(25):
            layer_depth = 0

            while image[layer_depth][i][j] == 2:
                layer_depth += 1

            row.append(image[layer_depth][i][j])
        res.append(row)
    return res


if __name__ == "__main__":
    """
    * Image consists of identically sized layers
    * Each layer has a fiexd width and height
    * WIDTH : 25, HEIGHT: 6
    * 0 -> BLACK, 1 -> WHITE, 2 -> TRANSPARENT
    """

    seq = list(map(int, list(open("8.txt", "r").read())))
    WIDTH = 25
    HEIGHT = 6
    p_per_layer = WIDTH * HEIGHT
    num_layers = len(seq)//p_per_layer

    # Part 1

    digit_count = []
    for i in range(num_layers):
        zeros = num_zeros(seq[i*p_per_layer:(i+1)*p_per_layer])
        ones = num_ones(seq[i*p_per_layer:(i+1)*p_per_layer])
        twos = num_twos(seq[i*p_per_layer:(i+1)*p_per_layer])
        digit_count.append((zeros, ones, twos))

    digit_count = sorted(digit_count, key=lambda x: x[0])
    print(digit_count[0][1] * digit_count[0][2])

    # Part 2

    # Create a list of lists, representing the layers
    # [[layer1 .. [row1 .. WIDTH], [row2 .. WIDTH] ], [layer2]]

    image = []
    for i in range(num_layers):
        layer = []
        layer_data = seq[i*p_per_layer:(i+1)*p_per_layer]
        for c in range(HEIGHT):
            layer.append(layer_data[c*WIDTH:(c+1)*WIDTH])
        image.append(layer)

    res = decode_image(image)
    plt.imshow(res)
    plt.show()
