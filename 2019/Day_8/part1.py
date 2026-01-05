content = open("input1.txt","r").read()

layer_size = 25*6
layers = []

i=0
while i<len(content):
    layers.append(content[i:i+layer_size])
    i+=layer_size

min_zeros = float("inf")
res = 0

for layer in layers:
    zero_count = layer.count("0")
    if  zero_count < min_zeros:
        one_count = layer.count('1')
        two_count = layer.count('2')
        res = one_count * two_count
        min_zeros = zero_count

print(res)