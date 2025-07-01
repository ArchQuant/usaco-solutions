import sys
sys.stdin = open("input", "r")

import math
def prime_enumerate(N):
    is_prime = [True] * (N + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N + 1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

L, R = map(int, input().split())
vis = [0] * (R - L)
ans = 1
for p in prime_enumerate(int(math.isqrt(R)) + 100):
    start = max((L // p + 1) * p, p * p)
    for x in range(start, R + 1, p):
        idx = x - (L + 1)
        if idx < 0 or vis[idx]:
            continue
        vis[idx] = 1
        y = x
        while y % p == 0:
            y //= p
        if y == 1:
            ans += 1
ans += vis.count(0)
print(ans)