
def solve(s):
    l = list(s)
    l[0] = l[0].upper()
    for i in range(len(l)):
        if l[i] == ' ':
            l[i+1] = l[i+1].upper()
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    print(solve(s))

# s = 'hello world'
# print(s[:].split())
