import math

content = open("input1.txt","r").read()
lines = content.split("\n")

totalMass = 0

for line in lines:
    # print(line)
    num = int(line)
    a = math.floor(num/3)
    # print(a)
    b = a - 2
    totalMass += b

print("Final Answer: ",totalMass)