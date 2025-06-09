import sys
sys.stdin = open("input", "r")

farm_num, query_num = map(int, input().split())
farms = input()
neighbors = [[] for _ in range(farm_num)]
for _ in range(farm_num - 1):
    f1, f2 = map(lambda x: int(x) - 1, input().split())
    neighbors[f1].append(f2)
    neighbors[f2].append(f1)

queries = [input().split() for _ in range(query_num)]
queries = [(int(a) - 1, int(b) - 1, c) for a, b, c in queries] # 0-index

# method 1: Union-Find
reps = list(range(farm_num))

def find(x):
    if reps[x] != x:
        reps[x] = find(reps[x])
    return reps[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py: # no need for rank here, just group
        reps[py] = px

# same-type connected farms
for i in range(farm_num):
    for j in neighbors[i]:
        if farms[i] == farms[j]:
            union(i, j)

for a, b, milk in queries:
    if find(a) == find(b):
        print(1 if farms[a] == milk else 0, end="") # end="" so no new line 
    else:
        print(1, end="")


# method 2: iterative DFS
component_num = 0
component = [-1 for _ in range(farm_num)]
for f in range(farm_num):
	if component[f] != -1:
		continue
	stack = [f]
	curr_type = farms[f]
	while stack:
		curr = stack.pop()
		component[curr] = component_num
		for n in neighbors[curr]:
			if farms[n] == curr_type and component[n] == -1:
				stack.append(n)
	component_num += 1

for a, b, milk in queries:
    if component[a] == component[b]:
        print(1 if farms[a] == milk else 0, end="") # end="" so no new line
    else:
        print(1, end="")

