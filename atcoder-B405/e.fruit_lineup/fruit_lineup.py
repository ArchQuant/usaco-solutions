import sys
sys.stdin = open("input", "r")
MOD = 998244353
N = int(4e6 + 5)
a,b,c,d = [int(i) for i in input().split()]
n = a + b + c + d

# Fast exponentiation mod x^y, O(logN)
def expo(x, y):
    res = 1
    while y:
        if y & 1:
            res = res * x % MOD
        x = x * x % MOD
        y >>= 1
    return res

# Precompute factorials and inverse factorials
fact = [1] * (N)
inv_fact = [1] * (N)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD

# Fermat's little theorem to calculate modular inverse factorial
# for prime p, a^p = a (mod p)  ->  a * a^(p-2) = a^(p-1) = 1 (mod p)
# so a^(p-2) is a modular multiplicative inverse of a
inv_fact[n] = expo(fact[n], MOD - 2)

for i in range(n - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

# comb(x, y) is the number of ordering with x of fruit A, and y of fruit B
# see Extended question below.
def comb(x, y):
    return fact[x + y] * inv_fact[x] % MOD * inv_fact[y] % MOD

# A <- C
# A <- D
# B <- D 
# divide into to three groups: (a-1, b-i), A, (c, d+i)
# i is part of b, i.e., a mixed with part of b, then c/d mixed with remaining b
# these two groups can be placed side by side.
# IM - place A in between to avoid duplicate count, 
# because B could appear both in (c, d+i) and (a-1, b-i). 
# e.g. (AB)(CD) and (A)(BCD) are double counted. 
# Put A mid to only count once as ()A(BCD)
ans = 0
for i in range(b + 1):
    ans = (ans + comb(b - i, a - 1) * comb(c, i + d) % MOD) % MOD
print(ans)

'''
How many ways to pick n items from m types with repetition.

Answer: NOT m * n, because of duplicate, for example, 
different orders 112 vs 211 are the same.

Thing placing n stars in m buckets, each star means one selection.
n stars: ****
m buckets with (m-1) bars:  |||
after placement: *||**|*

So there are total (n+m-1) in the end, select n:  C(n+m-1, n).

Extented question: a number of ball A, b number of ball B. 
How many ways to arrange them (within A, balls are indistinguishable).

Method 1: select a out of (a+b): C(a+b, a)
Method 2: pick a out of b+1 possible insert positions, thus n=a, m=b+1.
C(n+m-1, n)  = C(a+b, a)
'''