# import re
# string = 'aaadaa'
# substring = 'aa'
# subs = re.compile(substring)
# print(subs)
# matches = subs.search(string)
# # matches_positions = [(match.start(),match.end()-1) for match in matches]
# # print(matches_positions)
# # m = re.findall('aa',string)
# # print(m)
# print(matches)
S = 'aaadaa'
k = 'aa'
import re
pattern = re.compile(k)
print(pattern)
r = pattern.search(S)
print(r)
# if not r: print "(-1, -1)"
# while r:
#     print "({0}, {1})".format(r.start(), r.end() - 1)
#     r = pattern.search(S,r.start() + 1)