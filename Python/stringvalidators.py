'''
                                  any               all
All truthy values                  T                 T
All falsy values                   F                 F
one T all F                        T                 F
one F all T                        T                 F
Empty                              F                 T
'''


if __name__ == '__main__':
    s = input()
    print(any([char.isalnum() for char in s]))
    print(any([char.isalpha() for char in s]))
    print(any([char.isdigit() for char in s]))
    print(any([char.islower() for char in s]))
    print(any([char.isupper() for char in s]))