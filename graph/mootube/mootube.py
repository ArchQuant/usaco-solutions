# IM: The key sentence in question which indicates a tree structure:
# FJ has picked his N−1 pairs so that any video can be reached from any other video 
# along a path of connections in exactly one way.

# IM: During travesal: only traverse edges >= the relevance threshold.

import sys
sys.stdin = open("input", "r")

# Q: how is this value picked?
sys.setrecursionlimit(int(1e9))


def dfs(v: int, threshold: int) -> None:
	global num_reachable
	visited[v] = True
	for n in neighbors[v]:
		# Only visit non-visited vertices >= current threshold
		if not visited[n[0]] and n[1] >= threshold:
			num_reachable += 1
			dfs(n[0], threshold)


neighbors = []
visited = []
num_reachable = 0
video_num, query_num = map(int, input().split())
neighbors = [[] for _ in range(video_num + 1)]
for _ in range(video_num - 1):
    a, b, relevance = map(int, input().split())
    a -= 1 # 0-index
    b -= 1
    neighbors[a].append((b, relevance))
    neighbors[b].append((a, relevance))

for _ in range(query_num):
    threshold, start = map(int, input().split())
    start -= 1

    # Reset global variables for the current query
    num_reachable = 0
    visited = [False] * video_num
    dfs(start, threshold)

    print(num_reachable)