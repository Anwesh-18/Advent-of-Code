content = open('input.txt').read()
lines = content.split('\n')

def has_abba(s):
    for i in range(len(s) - 3):
        a, b, c, d = s[i:i+4]
        if a == d and b == c and a != b:
            return True
    return False

count = 0

for line in lines:
    parts = []
    hypernets = []

    curr = ""
    inside = False

    for ch in line:
        if ch == '[':
            parts.append(curr)
            curr = ""
            inside = True
        elif ch == ']':
            hypernets.append(curr)
            curr = ""
            inside = False
        else:
            curr += ch

    if inside:
        hypernets.append(curr)
    else:
        parts.append(curr)

    if any(has_abba(p) for p in parts) and not any(has_abba(h) for h in hypernets):
        count += 1

print(count)
