content = open("input2.txt", "r").read()
lines = content.split("\n")

total_original = 0
total_encoded = 0

for line in lines:
    total_original += len(line)

    encoded = line.replace('\\', '\\\\').replace('"', '\\"')
    encoded = '"' + encoded + '"'

    total_encoded += len(encoded)

print(total_encoded - total_original)