from itertools import combinations


def combine(string, num):
    for i in range(1, num + 1):
        for j in combinations(sorted(string), i):
            print(''.join(j))


str, num = input().split()
combine(str, int(num))
