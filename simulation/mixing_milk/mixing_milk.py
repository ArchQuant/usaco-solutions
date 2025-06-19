import sys
sys.stdin = open("input", "r")

cap = [0] * 3 # capacity
amt = [0] * 3 # actual amount

for k in range(3):
    cap[k], amt[k] = [int(i) for i in input().split()]

for i in range(100):
    cur = i % 3 # find the current pair of pouring
    nxt = (cur + 1) % 3

    # A->B = min(B-b, a)
    poured = min(cap[nxt] - amt[nxt], amt[cur])
    amt[cur] -= poured
    amt[nxt] += poured

for a in amt:
    print(a)

