import sys
sys.stdin = open("input","r")

from itertools import permutations

n, m = [int(i) for i in input().split()]
edges = []
    
f = [[False]*n for _ in range(n)]
for i in range(m):
    u, v = [int(i)-1 for i in input().split()]
    if u > v:
        u, v = v, u
    f[u][v] = True

ans = 100
# IM: 2-regular graph means must be cycle/cycles
# total 8 vertex, so max 2 cycles
for a in permutations(range(n)): # this is the sequence of the cycle vertex
    # Cycle * 1
    g = [[False]*n for _ in range(n)]
    for i in range(n):
        u, v = a[i], a[(i + 1) % n]
        if u > v:
            u, v = v, u
        g[u][v] = True
    c0 = sum(f[i][j] != g[i][j] for i in range(n) for j in range(n))
    ans = min(ans, c0)

    # Cycle * 2
    for d in range(3, n - 2 + 1):
        h = [[False]*n for _ in range(n)]
        # First cycle of size d
        for i in range(d):
            u, v = a[i], a[(i + 1) % d]
            if u > v:
                u, v = v, u
            h[u][v] = True
        # Second cycle of size n - d
        for i in range(n - d):
            idx1 = i + d
            idx2 = (i + 1) % (n - d) + d
            u, v = a[idx1], a[idx2]
            if u > v:
                u, v = v, u
            h[u][v] = True
        c1 = sum(f[i][j] != h[i][j] for i in range(n) for j in range(n))
        ans = min(ans, c1)

print(ans)


""" ETL
from itertools import combinations
def edge_id(u, v, N):
    if u > v:
        u, v = v, u
    return (u - 1) * N + (v - 1) - (u * (u - 1)) // 2

def generate_valid_degree_2_graphs(N):
    nodes = list(range(1, N + 1))
    all_edges = [(i, j) for i in nodes for j in nodes if i < j]
    edge_to_id = { (i,j): edge_id(i,j,N) for i,j in all_edges }

    valid_graphs = []

    for edge_subset in combinations(all_edges, N):
        deg = [0] * (N + 1)
        for u, v in edge_subset:
            deg[u] += 1
            deg[v] += 1
            if deg[u] > 2 or deg[v] > 2:
                continue
        if all(d == 2 for d in deg[1:]):
            valid_graphs.append(set(edge_to_id[(u, v)] for u, v in edge_subset))
    return valid_graphs, edge_to_id

N, M = [int(i) for i in input().split()]
edges = []
for _ in range(M):
    u, v = [int(i) for i in input().split()]
    edges.append((u, v))
valid_graphs, edge_to_id = generate_valid_degree_2_graphs(N)

original = set()
for u, v in edges:
    eid = edge_to_id[(min(u, v), max(u, v))]
    original.add(eid)

min_ops = float('inf')
for valid in valid_graphs:
    ops = len(original - valid) + len(valid - original)
    min_ops = min(min_ops, ops)

print(min_ops)

"""