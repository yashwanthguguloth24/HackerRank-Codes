from itertools import permutations

def permute(string,num):
    l = list(permutations(string,num))
    res = [''.join(i) for i in l]
    for i in range(len(res)):
        print(res[i],end = '\n')

#short code
def permute1(string,num):
    for i in list(permutations(sorted(string),num)):
        print(''.join(i))

str, num = input().split()
permute1(str,int(num))

