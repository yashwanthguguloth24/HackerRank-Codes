def minion_game(string):
    # your code goes here\
    vowels = 'AEIOU'
    string = string.upper()
    c1 = 0
    c2 = 0
    for i in range(len(string)):
        if string[i] in vowels:
            c1 += len(string)-i 
        else:
            c2 += len(string)-i
    if c2 > c1:
        print('Stuart',c2)
    elif c2 < c1:
        print('Kevin',c1)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)