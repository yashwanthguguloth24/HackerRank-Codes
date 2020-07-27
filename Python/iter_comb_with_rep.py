from itertools import combinations_with_replacement as ce


def combine_with_rep(string, num):
    for j in ce(sorted(string),num):
        print(''.join(j))


str, num = input().split()
combine_with_rep(str, int(num))