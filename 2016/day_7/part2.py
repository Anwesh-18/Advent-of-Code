content = open('input.txt').read()
lines = content.split('\n')

def get_ABAs(s):
    abas = set()
    for i in range(len(s) - 2):
        a, b, c = s[i:i+3]
        if a == c and a != b:
            abas.add(a + b + a)
    return abas

def supports_ssl(parts, hypernets):
    abas = set()
    for p in parts:
        abas |= get_ABAs(p)

    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        for h in hypernets:
            if bab in h:
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

    if supports_ssl(parts, hypernets):
        count += 1

print(count)
