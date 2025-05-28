import sys
sys.stdin = open("input", "r")

# the perimeter is not counting the neighbors, but the edges
# i.e., 
# . . 1 # #
# . . . 2 #
# for this case, the perimeter at 2 is 2, not 1, because two cells have one edge each

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

n = int(input())
grid = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
print(grid)

# DFS floodfill: from start point, mark all reachables as True
# also use mark as visited to avoid duplicate
def dfs(r0, c0):
    stack = [(r0, c0)]
    visited[r0][c0] = True # don't forget to mark the start point!
    area = perimeter = 0
    while stack:
        r, c = stack.pop()
        area += 1
        perimeter += 4
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<n and 0<=nc<n and grid[nr][nc] == '#':
                perimeter -= 1  # this is not an edge because ajacent to another '#'
                if not visited[nr][nc]:
                    stack.append((nr, nc))
                    visited[nr][nc] = True
    return area, perimeter

max_area = -1
max_perimeter = -1
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == '#':
            area, perimeter = dfs(i, j)
            if area > max_area or (area == max_area and perimeter > max_perimeter):
                max_area = area
                max_perimeter = perimeter
print(max_area, max_perimeter)
