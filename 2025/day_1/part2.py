content = open('input.txt','r').read()
rotations = content.split('\n')

pointer = 50
password = 0

def rotate_right(num):
    global pointer, password
    for i in range(num):
        pointer = (pointer+1)%100
        if pointer == 0:
            password += 1

def rotate_left(num):
    global pointer, password
    for i in range(num):
        pointer = (pointer - 1) % 100
        if pointer == 0:
            password += 1


for rotation in rotations:
    dir = rotation[0]
    num = int(rotation[1:])

    if dir == 'R':
        rotate_right(num)
    elif dir == 'L':
        rotate_left(num)

    print(pointer,password)

    # if pointer == 0:
    #     password += 1

print(password)