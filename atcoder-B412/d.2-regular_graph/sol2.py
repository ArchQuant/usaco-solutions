def min_operations(N, M, edges):
    # Initial edge set as a set of sorted tuples
    initial = set(tuple(sorted((a, b))) for a, b in edges)
    
    # Build adjacency list for degree tracking
    adj = [[] for _ in range(N + 1)]
    degrees = [0] * (N + 1)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
        degrees[a] += 1
        degrees[b] += 1
    
    # Generate valid degree-2 graphs using DFS to build cycles
    def dfs(path, used_edges, start):
        if len(path) == N and start in adj[path[-1]]:  # Complete a cycle
            edges_set = set(tuple(sorted((path[i], path[(i + 1) % N]))) for i in range(N))
            if all(degrees[v] + (v in path) * 2 == 2 for v in range(1, N + 1)):
                valid_graphs.append(edges_set)
            return
        for v in range(1, N + 1):
            if v not in path and (path[-1], v) in used_edges:
                path.append(v)
                dfs(path, used_edges, start)
                path.pop()
    
    valid_graphs = []
    all_possible_edges = set(tuple(sorted((i, j))) for i in range(1, N + 1) for j in range(i + 1, N + 1))
    for start in range(1, N + 1):
        dfs([start], all_possible_edges, start)
    
    # Find minimum operations
    min_ops = float('inf')
    for valid in valid_graphs:
        ops = len(initial - valid) + len(valid - initial)
        min_ops = min(min_ops, ops)
    
    return min_ops if min_ops != float('inf') else N  # Default to N if no valid graph found
import sys

sys.stdin = open("input","r")
# Input handling
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
result = min_operations(N, M, edges)
print(result)