import sys
sys.stdin = open("input", "r")

# find the longest contiguous array with sum divisible by 7

# IM - prefix, mod, record the first/last (both are size 7) 
first = [float('inf')] * 7 # use inf, not -1, so that we can use min
last = [0] * 7
first[0] = 0
curr_pref = 0

n = int(input())
for i in range(1, n + 1): # go through once, update first/last
    curr_pref += int(input())
    curr_pref %= 7
    first[curr_pref] = min(first[curr_pref], i) # IM - one liner, use min instead of if-else
    last[curr_pref] = i

ret = 0
for i in range(7):
    if first[i] != float('inf'):
        ret = max(ret, last[i] - first[i])

print(ret)
