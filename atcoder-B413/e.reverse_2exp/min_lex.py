import sys
sys.stdin = open("input", "r")

sys.setrecursionlimit(1 << 20)

t = int(input())

def min_lex(p):
    n = len(p)
    if n == 1:
        return p
    mid = n // 2
    left = min_lex(p[:mid])
    right = min_lex(p[mid:])
    opt1 = left + right
    opt2 = right + left
    return min(opt1, opt2)

for _ in range(t):
    N = int(input())
    P = [int(i) for i in input().split()]
    res = min_lex(P)
    print(" ".join(map(str, res)))