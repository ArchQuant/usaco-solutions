import sys
sys.stdin = open("input", "r")

# input 407
# output: 1 + 4 + 1 + 3 + 1 + 7 = 17

s = [int(i) for i in list(input())]

count = len(s)
# the difference is const, which is s[i-1]-s[i] (mod 10)
for i in range(1, len(s)):
    if (diff := s[i-1] - s[i]) >= 0: # IM - don't forget parenthes
        count += diff
    else:
        count += diff + 10

# from 0 to last digit
count += s[-1]
print(count)
    


