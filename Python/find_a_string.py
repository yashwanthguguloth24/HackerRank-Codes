# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.
# Sample Input
# ABCDCDC
# CDC
# Sample Output
# 2

def count_substring(string, sub_string):
    # should include overlapping ones
    start = 0
    count = 0
    while start < len(string):
        finder = string.find(sub_string, start)
        if finder > -1:
            start = finder + 1
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)