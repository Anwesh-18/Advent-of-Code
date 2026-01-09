content = open("input.txt","r").read()
lines = content.split("\n")

item_data = {}

for line in lines:
    line = line.rstrip(",").split()
    item = line[0].rstrip(":")
    cap = int(line[2].rstrip(","))
    dur = int(line[4].rstrip(","))
    flav = int(line[6].rstrip(","))
    text = int(line[8].rstrip(","))
    cal = int(line[10])

    if item not in item_data:
        item_data[item] = [cap, dur, flav, text,cal]

best = 0

def calc_score(item_data,num,id):
    res = 0
    idx = 0
    for item in item_data:
        res += item_data[item][num]*id[idx]
        idx += 1

    return res

for a in range(101):
    for b in range(101-a):
        for c in range(101-b-a):
            d = 100-a-b-c
            f_cap = max(0,calc_score(item_data,0,[a,b,c,d]))
            f_dur = max(0,calc_score(item_data,1,[a,b,c,d]))
            f_flav = max(0,calc_score(item_data,2,[a,b,c,d]))
            f_text = max(0,calc_score(item_data,3,[a,b,c,d]))
            f_cal = max(0,calc_score(item_data,4,[a,b,c,d]))
            score = f_cap * f_dur * f_flav * f_text
            if f_cal == 500:
                best = max(best,score)

print(best)