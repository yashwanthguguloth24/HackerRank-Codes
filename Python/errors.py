for i in range(int(input())):
    s = input().split()
    try:
        a = int(s[0])//int(s[1])
        print(a)
    except ZeroDivisionError as z:
        print('Error Code:',z)
    except ValueError as v :
        print('Error Code:',v)

