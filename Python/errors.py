for i in range(int(input())):
    s = input().split()
    try:
        a = int(s[0])//int(s[1])
        print(a)
    except ZeroDivisionError as zs:
        print('Error Code:',zs)
    except ValueError as ve :
        print('Error Code:',ve)

