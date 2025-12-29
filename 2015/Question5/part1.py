content = open("input1.txt","r").read().splitlines()

count = 0
def isNice(line):
    vowels = ["a","e","i","o","u"]
    vCount = 0
    second = False
    check = ["ab","cd","pq","xy"]
    third = False
    # checking for 3 vowels
    for char in line:
        if char in vowels:
            vCount += 1
            if(vCount >= 3):
                break
    # checking for duplets
    for i in range(1,len(line)):
        if line[i]==line[i-1]:
            second = True
            break
    # checking for ab,cd,pq,xy
    for i in range(len(line)):
        if line[i:i+2] in check:
            third = True
            break
    if (vCount >= 3) and second and not third:
        return True
    return False

for line in content:
    if isNice(line):
        count += 1

print(count)