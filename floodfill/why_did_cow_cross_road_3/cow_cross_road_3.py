



import sys
sys.stdin = open("input","r")

side_len, cow_num, road_num = [int(i) for i in input().split()]
roads = set()
for _ in range(road_num):
    sr, sc, er, ec = [int(i) - 1 for i in input().split()] # 0-index
    roads.add((sr, sc, er, ec)) # IM: use field coordinates to store roads
    roads.add((er, ec, sr, sc))

has_cow = [[False for _ in range(side_len)] for _ in range(side_len)]
for _ in range(cow_num):
    r, c = [int(i) - 1 for i in input().split()] # 0-index
    has_cow[r][c] = True

visited = [[False] * side_len for _ in range(side_len)]

def neighbors(r: int, c: int):
	return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

# IM: recursive: loop each neighbor and sum up the unvisited && connected cows
def connected_cow_num(r: int, c: int, prev_r: int, prev_c: int):
	if (
		r < 0
		or c < 0
		or r >= side_len
		or c >= side_len
		or visited[r][c]
		or (r, c, prev_r, prev_c) in roads # cross a road
	):
		return 0

	visited[r][c] = True
	cow_num = has_cow[r][c]
	for nr, nc in neighbors(r, c):
		cow_num += connected_cow_num(nr, nc, r, c)
	return cow_num


cow_components = [] # append the size of each components
for r in range(side_len):
	for c in range(side_len):
		if not visited[r][c]:
			comp_sz = connected_cow_num(r, c, r, c)
			if comp_sz != 0:
				cow_components.append(comp_sz)

distant_pairs = 0
for i in range(len(cow_components)):
	for j in range(i + 1, len(cow_components)):
		# each components pair up
		distant_pairs += cow_components[i] * cow_components[j]

print(distant_pairs)