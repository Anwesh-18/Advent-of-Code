with open("input2.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    l,h,w = map(int,line.split("x"))
    first = min(2*(l+w),2*(w+h),2*(h+l))
    second = l*w*h
    total += first + second

print(total)