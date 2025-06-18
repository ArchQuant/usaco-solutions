import sys
sys.stdin = open("input", "r")

N, H, M = [int(i) for i in input().split()]
A = []
B = []
for i in range(N):
    a, b = [int(i) for i in input().split()]
    A.append(a)
    B.append(b)

# IM: dp[i][h] is the max magic after i-th monster, with h health
# 1. H first, N second loop; 2. padding for initial state
dp = [[-1] * (H + 1) for _ in range(N + 1)] 
# boundary
dp[0][H] = M  # Start with full health and magic
max_defeat = 0

for i in range(N):
    for h in range(H + 1):
        # at initial, can only have H and M
        # then one-by-one monster
        if dp[i][h] == -1:
            continue
        m = dp[i][h]
        # Option 1: Fight using magic
        if m >= B[i]:
            dp[i + 1][h] = max(dp[i + 1][h], m - B[i])
            max_defeat = max(max_defeat, i + 1)
        # Option 2: Fight using health
        if h >= A[i]:
            dp[i + 1][h - A[i]] = max(dp[i + 1][h - A[i]], m)
            max_defeat = max(max_defeat, i + 1)

print(max_defeat)




sys.setrecursionlimit(int(1e9))
import functools

# Exceed time limit: need to switch to bitset
# IM: dp is the max of the following max, not the previous max
@functools.cache
def dp(i, h, m):
    if i >= N:
        return 0
    
    max_defeated = 0
    if h >= A[i]:
        max_defeated = max(max_defeated, 1 + dp(i + 1, h - A[i], m))
    if m >= B[i]:
        max_defeated = max(max_defeated, 1 + dp(i + 1, h, m - B[i]))
    
    return max_defeated

print(dp(0, H, M))