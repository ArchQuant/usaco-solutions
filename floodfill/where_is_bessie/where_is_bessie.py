import sys
sys.stdin = open("input", "r")

# IM: since N < 20, use brute force

# Containment rule: a PCL should not be contained within another PCL
# i.e., need to find the largest PCLs

# IM: Don't set containment rules in the looping index, just hit each index and check the rules
# at start of each loop, check if the current rectangle is a smaller PCL of existing, if so, skip it
# at end of each loop, check if the current rectangle is a larger PCL of existing, if so, remove the smaller ones

from collections import defaultdict

N = int(input())
grid = [[ord(c) - ord('A') for c in list(input())] for _ in range(N)]
pcl_list = []  # stores PCLs as [i1, j1, i2, j2]

def is_pcl(i1, j1, i2, j2):
    visited = [[False] * N for _ in range(N)]
    regions = defaultdict(int)

    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            if visited[i][j]:
                continue
            color = grid[i][j]
            stack = [(i, j)]
            visited[i][j] = True
            while stack:
                x, y = stack.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if i1 <= nx <= i2 and j1 <= ny <= j2 and not visited[nx][ny] and grid[nx][ny] == color:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            regions[color] += 1
            if len(regions) > 2:
                return False
    if len(regions) != 2:
        return False
    # check rule: color1 has 1 region, color2 > 1 region
    num_color1, num_color2 = sorted(regions.values())
    return num_color1 == 1 and num_color2 > 1


# IM: a rectangle is defined by two corners (i1, j1) and (i2, j2)
for i1 in range(N):
    for j1 in range(N):
        for i2 in range(i1, N):
            for j2 in range(j1, N):
                if (i2 - i1 + 1) * (j2 - j1 + 1) < 2:
                    continue
                # skip if contained in an existing PCL
                if any(i1 >= a and j1 >= b and i2 <= c and j2 <= d for a, b, c, d in pcl_list):
                    continue
                if is_pcl(i1, j1, i2, j2):
                    # Remove the existing smaller PCLs that's fully contained in this one
                    pcl_list = [p for p in pcl_list if not (i1 <= p[0] and j1 <= p[1] and i2 >= p[2] and j2 >= p[3])]
                    pcl_list.append([i1, j1, i2, j2])

print(len(pcl_list))
