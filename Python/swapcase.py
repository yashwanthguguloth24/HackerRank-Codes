def swap_case(s):
    arr = list(s)
    new = []
    for i in range(0,len(arr)):
        if s[i].isupper():
            new.append(s[i].lower())
        else:
            new.append(s[i].upper())
    return "".join(new)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)