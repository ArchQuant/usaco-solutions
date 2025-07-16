import sys
sys.stdin = open("input", "r")

def is_palindrome(digits):
    return digits == digits[::-1]

def to_base_digits(n, base):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    return digits # reversed

def generate_palindromes(N):
    i = 1
    while True:
        # Odd-length palindrome
        s = str(i)
        p = int(s + s[-2::-1])
        if p > N:
            break
        yield p
        # Even-length palindrome
        p = int(s + s[::-1])
        if p <= N:
            yield p
        i += 1

A = int(input())
N = int(input())

total = 0
for num in generate_palindromes(N):
    if is_palindrome(to_base_digits(num, A)):
        total += num

print(total)
