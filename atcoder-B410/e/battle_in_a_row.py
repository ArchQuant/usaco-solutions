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