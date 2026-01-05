import json

content = open("input.txt","r").read()
data = json.loads(content)

def sum_numbers(obj):
    if isinstance(obj,int):
        return obj

    if isinstance(obj,list):
        return sum(sum_numbers(x) for x in obj)

    if isinstance(obj,dict):
        if "red" in obj.values():
            return 0
        return sum(sum_numbers(v) for v in obj.values())
    return 0

print(sum_numbers(data))