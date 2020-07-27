array = []
for i in range(int(input())):
    s = input().split()
    # we need convert values to int
    for j in range(1, len(s)):
        s[j] = int(s[j])

    # cases
    if s[0] == "insert":
        array.insert(s[1], s[2])
    elif s[0] == 'print':
        print(array)
    elif s[0] == 'remove':
        array.remove(s[1])
    elif s[0] == 'append':
        array.append(s[1])
    elif s[0] == 'sort':
        array.sort()
    elif s[0] == 'pop':
        array.pop()
    elif s[0] == 'reverse':
        array.sort(reverse=True)

# [1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
# [5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
# [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]

# [1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
# [87, 75, 75, 67, 66, 48, 44, 44, 30, 21, 12, 10, 9, 8, 7, 6, 5, 3, 2, 1]
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
# [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]