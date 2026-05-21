content = open('input.txt').read()

def decode(s):
    i = 0
    new_line = ''
    while i < len(s):
        if s[i] == '(':
            j = i
            while s[j] != ')':
                j += 1

            ch, rep = map(int, s[i + 1:j].split('x'))

            segment = s[j + 1: j + 1 + ch]
            new_line += segment * rep

            i = j + 1 + ch
        else:
            new_line += s[i]
            i += 1

    return new_line


res = len(decode(content))
print(res)