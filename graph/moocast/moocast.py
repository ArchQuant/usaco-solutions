import sys
sys.stdin = open("input", "r")
cow_num = int(input())
x = [0] * cow_num
y = [0] * cow_num
power = [0] * cow_num
for c in range(cow_num):
    x[c], y[c], power[c] = [int(i) for i in input().split()]

# IM: instead of build a graph of each pair, use a matrix "connected"
connected = [[False for _ in range(cow_num)] for _ in range(cow_num)]
for i in range(cow_num):
	for j in range(cow_num):
		dist_squared = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
		connected[i][j] = dist_squared <= power[i] ** 2

# recursive: reachable_cows(c) = sum of reachable_cows(c_neighbors)
def reachable_cows(c: int) -> int:
	""":return: how many cows can be reached from a cow c"""
	global visited
	visited[c] = True # mark self as visited
	reached = 1  # we can always reach the initial cow c
	for nc in range(cow_num):
		if not visited[nc] and connected[c][nc]:
			visited[nc] = True
			reached += reachable_cows(nc)
	return reached

max_cows = 0
for c in range(cow_num):
	visited = [False for _ in range(cow_num)] # reset for each loop
	max_cows = max(max_cows, reachable_cows(c))

print(max_cows)