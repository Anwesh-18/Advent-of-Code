import math

content = open("input2.txt","r").read()
lines = content.split("\n")

totalMass = 0

def calFuel(num):
    currFuel = 0
    while num != 0:
        num = math.floor(num/3)
        num = max(num - 2,0)
        currFuel += num

    return currFuel

for line in lines:
    num = int(line)
    fuel = calFuel(num)
    totalMass += fuel

print("Final Answer: ",totalMass)