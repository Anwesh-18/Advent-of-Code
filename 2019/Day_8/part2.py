content = open("input1.txt","r").read()

layer_size = 25*6
layers = []

i=0
while i<len(content):
    layers.append(content[i:i+layer_size])
    i+=layer_size

final_image = []

for pixel_index in range(layer_size):
    for layer in layers:
        pixel = layer[pixel_index]
        if pixel != "2":
            final_image.append(pixel)
            break

for row in range(6):
    start = row*25
    end = start + 25
    line = final_image[start:end]

    for pixel in line:
        if pixel == "1":
            print("#", end="")
        else:
            print(" ", end="")
    print()
        