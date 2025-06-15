import heapq
import sys
sys.stdin = open("input", "r")

def min_xor_walk(N, M, edges):
    # Graph representation: adjacency list with weights
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b, w = edges[i]
        graph[a].append((b, w))
    
    # Priority queue: (current_xor, vertex)
    pq = [(0, 1)]  # Start at vertex 1 with XOR 0
    visited = set()  # Track (xor, vertex) states to avoid cycles
    ret = []
    
    while pq:
        curr_xor, u = heapq.heappop(pq)
        
        if u == N:
            ret.append(curr_xor)
        
        state = (curr_xor, u) # use state to terminate search
        if state in visited:
            continue
        visited.add(state)
        
        for v, w in graph[u]:
            new_xor = curr_xor ^ w
            new_state = (new_xor, v)
            if new_state not in visited:
                heapq.heappush(pq, (new_xor, v))
    
    return [-1] if not ret else ret

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

result = min_xor_walk(N, M, edges)
print(min(result))