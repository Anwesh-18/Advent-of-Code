content = open("input1.txt","r").read()
ranges = content.split("-")

start = int(ranges[0])
end = int(ranges[1])
# print(start,end)

def isSameDigit(num):
    chars = list(str(num))
    for i in range(1,len(chars)):
        if chars[i] == chars[i-1]:
            return True
    return False

def isIncreasing(num):
    chars = list(str(num))
    for i in range(1,len(chars)):
        if int(chars[i]) < int(chars[i-1]):
            return False
    return True

res = 0

for i in range(start,end+1):
    if isSameDigit(i) and isIncreasing(i):
        res += 1

print(res)