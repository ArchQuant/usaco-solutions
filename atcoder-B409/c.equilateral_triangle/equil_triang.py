import sys
sys.stdin = open("input", "r")

n, l = [int(i) for i in input().split()]
ds = [int(i) for i in input().split()]

if not l % 3 == 0:
    print(0)
    exit()

pos_count = [0] * l
pos_count[0] = 1 # initial is one
cur = 0
for d in ds:
    cur = (cur + d) % l
    pos_count[cur] += 1

ans = 0
for i in range(0, l//3, 1):
    ans += pos_count[i] * pos_count[i+l//3] * pos_count[i+l//3*2]
print(ans)

