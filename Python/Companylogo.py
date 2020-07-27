str = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
k = list(alphabets)
z = [0]*26

stack = [[i,j] for i,j in zip(k,z)]
# print(stack[0][1])

s_lst = list(str)
for let in s_lst:
    for i in range(0,len(k)):
        if let == k[i]:
            stack[i][1] += 1

z = []
for i in range(0,len(k)):
    if stack[i][1] > 1:
        z.append(stack[i])

k = sorted(z,key = lambda x: x[1],reverse = True)

for i in range(len(k)):
    print(k[i][0],k[i][1])


