import sys
from sys import setrecursionlimit

setrecursionlimit(10**5)

sys.stdin = open("input", "r")

# cannot use namedTuple, because visited is mutable
class Cow:
	def __init__(self, x, y, adj, visited):
		self.x = x
		self.y = y
		self.adj = adj
		self.visited = visited

# flood fill
def connected_cows(cows, start):
	net = []
	def dfs(curr: int) -> None:
		cows[curr].visited = True
		net.append(curr)
		for c in cows[curr].adj:
			if not cows[c].visited:
				dfs(c)

	dfs(start)
	return net

cows = []

n, m = [int(i) for i in input().split()]

for _ in range(n):
    x, y = [int(i) for i in input().split()]
    cows.append(Cow(x, y, [], False))

for _ in range(m):
    a, b = [int(i) - 1 for i in input().split()]
    cows[a].adj.append(b)
    cows[b].adj.append(a)

networks = []
for c in range(n):
	if not cows[c].visited:
		networks.append(connected_cows(cows, c))

min_perimeter = float("inf")
for net in networks:
	min_x = float("inf")
	max_x = 0
	min_y = float("inf")
	max_y = 0
	for c in net:
		c = cows[c]
		min_x = min(min_x, c.x)
		max_x = max(max_x, c.x)
		min_y = min(min_y, c.y)
		max_y = max(max_y, c.y)

	min_perimeter = min(min_perimeter, 2 * (max_x - min_x) + 2 * (max_y - min_y))

print(min_perimeter)