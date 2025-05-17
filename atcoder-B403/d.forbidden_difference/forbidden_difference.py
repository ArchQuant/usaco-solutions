# IM - although requires absolute diff, we still only need forward scan.
# because C(x-d) = 0 AND C(x+d) = 0 for all x, is equivalent to
# C(x+d) = 0 for all x in order 0->n

# Decompose to independent sub-tasks:
# arr[::d] means A0, A1, A2,... -> Ai, Ai+d, Ai+2d, Ai+3d,...Ai+kd, for i=0,...d-1
# IM - here arr need to pad with zeros to cover all integers

# IM - related to find global minimum, use DP:
# dp[k] is the minimum required removals upto point k, for k = 0,...N//d
# dp[k+1] = min(dp[i] + Count(Ak+1), dp[i-1] + Count(Ak)), ensure no consecutive neighbors
# boundary: dp[0]=0; direction:0->N//d

# IM - corner case d == 0

import sys
sys.stdin = open("input", "r")

from collections import defaultdict
N, D = map(int, input().split())
array = [int(i) for i in input().split()]

count = [0] * (10**6 + 1) # cover [0, 10**6]
array.sort()
for num in array:
    count[num] += 1

def get_min_removal(arr):
    if not arr: # check empty
        return 0
    dp = [0] * len(arr)
    for k in range(len(arr)-1): # general note: (0, len-1) with k+1, or (1, len) with k
        dp[k+1] = min(dp[k]+arr[k+1], dp[k-1]+arr[k])
    return dp[-1]

ret = 0
if D == 0:
    # leave only distinct elem. subtract them from total
    print(N - sum([1 for i in count if i != 0]))
else:
    for i in range(D):
        ret += get_min_removal(count[i::D])
    print(ret)
    


