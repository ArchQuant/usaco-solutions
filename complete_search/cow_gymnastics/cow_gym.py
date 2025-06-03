import sys
sys.stdin = open("input", "r")

k, n = [int(i) for i in input().split()]
rank = [[int(i) for i in input().split()] for _ in range(k)]

pairs = []
# use the first ranking as a reference, and find contradiction in the rest of sessions
for i in range(n-1):
    for j in range(i+1, n):
        pairs.append((rank[0][i], rank[0][j]))

# Don't change during a loop, e.g.,
#for r in rank[1:]:
#    for p in pairs:
#        if r.index(p[0]) > r.index(p[1]):
#            pairs.remove(p)

count = 0
# IM: instead, put the pair in the outer loop
for p in pairs:
    for r in rank[1:]:
        if r.index(p[0]) > r.index(p[1]):
            break
    # use for-loop-else
    else:
        count += 1

print(count)

# method2: make a T/F matrix, where grid[a][b] = True when any a > b (not all)
# then check grid[a][b], grid[b][a], if only one is True, then consistent
# How to check? since a/b are different, at least one is True, so only need to check if both are True
# valid_count += (not grid[a][b] or not grid[b][a])