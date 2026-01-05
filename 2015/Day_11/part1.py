content = open("input.txt","r").read()
password = content

def next_pass(password):
    password = list(password)
    # print(password)
    for i in range(len(password)-1,-1,-1):
        if password[i] == 'z':
            password[i] = 'a'
        else:
            password[i] = chr(ord(password[i]) + 1)
            return ''.join(password)

    return 'a' * (len(password) + 1)

def check_pwd(password):
    double_count = 0
    password = list(password)

    for c in password:
        if c in ('i', 'o', 'l'):
            return False

    has_straight = False
    for i in range(len(password) - 2):
        if (
                ord(password[i]) + 1 == ord(password[i + 1]) and
                ord(password[i]) + 2 == ord(password[i + 2])
        ):
            has_straight = True
            break

    if not has_straight:
        return False
    i=1
    while i < len(password):
        if password[i] == password[i-1]:
            double_count += 1
            i+=2
            continue
        else:
            i+=1

    if double_count >= 2 :
        return True
    else:
        return False

found = False
while not found:
    password = next_pass(password)
    if check_pwd(password):
        print("Password found: ",password)
        found = True