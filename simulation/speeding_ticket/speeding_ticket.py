import sys
sys.stdin = open("input", "r")

n, m = [int(i) for i in input().split()]

limit_seg = [[int(i) for i in input().split()] for _ in range(n)]
actual_seg = [[int(i) for i in input().split()] for _ in range(m)]

limit = [] # decompose into 1-mile
for s in limit_seg:
	for _ in range(s[0]):
		limit.append(s[1])

actual = []
for s in actual_seg:
	for _ in range(s[0]):
		actual.append(s[1])

worst = 0
for a, b in zip(limit, actual):
	worst = max(worst, b - a)

print(worst)