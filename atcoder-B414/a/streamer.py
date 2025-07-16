import sys
sys.stdin = open("input", "r")

n, l, r = [int(i) for i in input().split()]
count = 0
for _ in range(n):
 x, y = [int(i) for i in input().split()]
 if x <= l and y >= r:
  count += 1

print(count)
