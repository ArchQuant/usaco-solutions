import sys
sys.stdin = open("input", "r")
MOD = 998244353
N = int(input())
ans = (N) * (N + 1) // 2

b = 1
while b <= N:
    q = N // b
    r = N // q + 1
    ans -= (q) * (r - b)
    b = r

print(ans % MOD)
