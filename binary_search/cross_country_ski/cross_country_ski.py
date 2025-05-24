from collections import deque
import sys
sys.stdin = open("input", "r")

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
MAX_N = 500

m, n = [int(i) for i in input().split()]
grid = [[int(i) for i in input().split()] for _ in range(m)]
wp = [[bool(int(i)) for i in input().split()] for _ in range(m)]
mark = [[False]*n for _ in range(m)]

# find a start point (any one of the waypoints)
r0, c0 = -1, -1
for i in range(m):
    for j in range(n):
        if wp[i][j]:
            r0, c0 = i, j
            break

# DFS floodfill: from start point, mark all reachables as True
# also use mark as visited to avoid duplicate
def dfs(d):
    stack = [(r0, c0)]
    mark[r0][c0] = True # don't forget to mark the start point!
    while stack:
        r, c = stack.pop()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<m and 0<=nc<n and not mark[nr][nc] and abs(grid[r][c]-grid[nr][nc]) <=d:
                stack.append((nr, nc))
                mark[nr][nc] = True

def reachable(d):
    global mark # use glbal within a function to change global list
    mark = [[False]*n for _ in range(m)]
    dfs(d)
    for i in range(m):
        for j in range(n):
            if wp[i][j] and not mark[i][j]:
                return False
    return True

# Binary search: FFFFFFFFTTT, i.e.,
# for all mid >= d, reachable(d) is true; 
l, r = 0, 1e9
res = -1
while l <= r:
    mid = (l + r) // 2
    if reachable(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)