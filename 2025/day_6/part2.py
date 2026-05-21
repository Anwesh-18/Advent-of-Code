content = open('input.txt','r').read()
lines = content.split('\n')

# print(lines[0].split(" "))
# print(lines[1].split(' '))
# print(lines[2].split(' '))
print(lines)
















# res = []
# set_len = True
#
# def rearrange(arr):
#     temp = [list(num) for num in arr[:-1]]
#     new_arr = []
#     while any(temp):
#         new_num = ""
#         for col in temp:
#             if col:
#                 new_num += col.pop()
#         new_arr.append(int(new_num))
#
#     return new_arr
#
# def mul(nums):
#     tm = 1
#     for num in nums:
#         tm *= num
#     return tm
#
# def compute(res,op):
#     if op == '+':
#         return sum(res)
#     else:
#         return mul(res)
#
# for line in lines:
#     line = line.split()
#     if set_len:
#         for i in range(len(line)):
#             temp = [line[i]]
#             res.append(temp)
#
#         set_len = False
#
#     else:
#         for i in range(len(line)):
#             if line[i] == '+' or line[i] == '*':
#                 res[i].append(line[i])
#             else:
#                 res[i].append(line[i])
#
# total = 0
# for ops in res:
#     op = ops[-1]
#     new_res = rearrange(ops)
#     print(new_res)
#     print(compute(new_res,op))
#     total += compute(new_res,op)
#
# print(total)