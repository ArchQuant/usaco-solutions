import sys
sys.stdin = open("input", "r")

n = int(input())
cs = [int(i) for i in input().split()]

counter = [0] * (n+1)

for c in cs:
    counter[min(c, n)] += 1

cumsum = 0
for i in range(n, -1, -1):
    cumsum += counter[i]
    if cumsum >= i:
        print(i)
        exit()
