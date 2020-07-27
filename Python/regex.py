import re
for i in range(int(input())):
    s = input()
    try:
        re.compile(s)
        is_valid = True
        print('True')
    except re.error:
        is_valid = False
        print('False')