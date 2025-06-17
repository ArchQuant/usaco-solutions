import sys
sys.stdin = open("input", "r")

sys.setrecursionlimit(int(1e9))
import functools


N, H, M = [int(i) for i in input().split()]
A = []
B = []
for i in range(N):
    a, b = [int(i) for i in input().split()]
    A.append(a)
    B.append(b)

# IM: dp[i][m] is the max health after i-th monster, with magic power m
dp = [-1] * (M + 1)
dp[M] = H  # Start with full health and magic

max_defeated = 0

for i in range(N):
    next_dp = [-1] * (M + 1)
    for m in range(M + 1):
        if dp[m] >= 0:
            # Option 1: Use health if possible
            if dp[m] >= A[i]:
                next_dp[m] = max(next_dp[m], dp[m] - A[i])
            # Option 2: Use magic if possible
            if m >= B[i]:
                next_dp[m - B[i]] = max(next_dp[m - B[i]], dp[m])
    if max(next_dp) < 0:
        break
    dp = next_dp
    max_defeated += 1

print(max_defeated)

# dp = [[-1] * N for _ in range(M)]




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