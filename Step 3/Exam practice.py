# a = [0, 1, 2]
# b = [1, 2, 0]

# for i in a:
#     for j in b:
#         i, j
#     return i+j
# print(i+j)
# goes over 1 and down 2. then goes down three, then goes down 1. The moves on to 1 in a and goes over 2, moves


# state diagram

# def(i):
#     for x in i:
#         if x == 2:
#             print(x)
#         elif x == 1:
#             print('a')
#     print("d")

# ^ function has a return value o# f none. It only returns a value if it explicitly says 'return'
a= [1,2,3,4]
print(a[2::-2])
for i in range(a[2]):
    print (i + 4)

a.append(5)
print(a)

short = [10, 4, 6]

short[2] = 2
print(short)