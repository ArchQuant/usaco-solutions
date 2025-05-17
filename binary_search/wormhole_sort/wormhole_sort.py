with open("input", "r") as f:
    cow_num, wormhole_num = map(int, f.readline().split())
    cow_pos = list(map(lambda x: int(x)-1, f.readline().split())) # 0-index

    adj = [[] for _ in range(cow_num)]
    max_width = 0
    for _ in range(wormhole_num):
        u, v, width = map(int, f.readline().split())
        u -= 1
        v -= 1
        adj[u].append((v, width))
        adj[v].append((u, width))
        max_width = max(max_width, width)

lo = 0
hi = max_width + 1
valid = -1

# iterative DFS: flood color to group the connected pos
# alternatives: Union Find
def dfs(start, comp_id, component, adj, min_width):
    stack = [start]
    while stack:
        curr = stack.pop()
        if component[curr] != -1: # not colored yet
            continue
        component[curr] = comp_id
        stack.extend(n for n, w in adj[curr] if component[n] == -1 and w >= min_width)


# General algo is binary search due to monotonic nature
while lo <= hi:
    mid = (lo + hi) // 2
    component = [-1] * cow_num
    comp_id = 0

    for i in range(cow_num):
        if component[i] != -1:
            continue
        dfs(i, comp_id, component, adj, mid)
        comp_id += 1

    if all(component[i] == component[cow_pos[i]] for i in range(cow_num)):
        valid = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(f"{-1 if valid == max_width + 1 else valid}")
