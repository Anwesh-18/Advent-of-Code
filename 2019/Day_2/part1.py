content = open("input1.txt","r").read()
myList = list(map(int, content.split(",")))

myList[1] = 12
myList[2] = 2

i = 0
while i < len(myList) and myList[i] != 99:
    if myList[i] == 1:
        myList[myList[i+3]] = myList[myList[i+1]] + myList[myList[i+2]]
        i += 4
    elif myList[i] == 2:
        myList[myList[i+3]] = myList[myList[i+1]] * myList[myList[i+2]]
        i += 4
    else:
        break

print(myList[0])
