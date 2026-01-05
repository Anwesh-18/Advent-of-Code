content = open("input1.txt","r").read()
lines = content.split("\n")

total_strings = 0
total_chars = 0

def evaluate(line,isString=False):
    if isString:
        return len(line)
    else:
        return len(eval(line))

for line in lines:
    total_strings += evaluate(line,True)
    total_chars += evaluate(line)

print(total_strings-total_chars)
