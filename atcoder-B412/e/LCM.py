import sys
sys.stdin = open("input", "r")

def sieve_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]

def count_distinct_lcms(L, R):
    MOD = 998244353
    primes = sieve_primes(int(1e7))
    current_lcm = 1
    distinct = set([current_lcm % MOD])
    
    for n in range(2, min(R + 1, int(1e7))):
        temp_lcm = current_lcm
        for p in primes:
            if p > n:
                break
            if n % p == 0:
                power = p
                while power <= n:
                    power *= p
                power //= p
                if n == power:
                    temp = 1
                    while power <= n:
                        temp = (temp * power) // gcd(temp, power)
                        power *= p
                    temp_lcm = (temp_lcm * temp) // gcd(temp_lcm, temp)
        current_lcm = temp_lcm
        distinct.add(current_lcm % MOD)
    
    # For n > 10^7, changes are rare, simulate within range
    last_lcm = current_lcm
    for n in range(max(L, int(1e7)), R + 1):
        changed = False
        for p in primes:
            if p > n:
                break
            if n % p == 0:
                power = p
                while power <= n:
                    power *= p
                power //= p
                if n == power:
                    changed = True
                    break
        if changed:
            for p in primes:
                if p > n:
                    break
                if n % p == 0:
                    temp = 1
                    power = p
                    while power <= n:
                        temp = (temp * power) // gcd(temp, power)
                        power *= p
                    last_lcm = (last_lcm * temp) // gcd(last_lcm, temp)
        distinct.add(last_lcm % MOD)
    
    return len(distinct)

from math import gcd
L, R = map(int, input().split())
print(count_distinct_lcms(L, R))