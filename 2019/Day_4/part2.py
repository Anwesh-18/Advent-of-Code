content = open("input1.txt","r").read()
ranges = content.split("-")

start = int(ranges[0])
end = int(ranges[1])
print(start,end)

def isSameDigit(num):
    chars = list(str(num))
    i = 0

    while i < len(chars):
        count = 1
        while i + 1 < len(chars) and chars[i] == chars[i + 1]:
            count += 1
            i += 1

        if count == 2:
            return True
        i += 1
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
        # print(i)
        res += 1

print(res)