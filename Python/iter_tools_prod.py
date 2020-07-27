from itertools import product
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
prod = list(product(A,B))
for i in range(len(prod)):
    print(prod[i],end = ' ')