import sys
sys.stdin = open("input", "r")

sys.setrecursionlimit(2 * 10**5 + 5) # IM - must have, to terminate DFS

n, m = map(int, input().split()) # num of nodes, num of edges
if m != n:
    print("No")
    exit()

adj = [[] for _ in range(n+1)]
vis = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v) # append because may have more than one
    adj[v].append(u)

for i in range(1, n + 1):
    if len(adj[i]) != 2:
        print("No")
        exit()

def DFS(u, parent):
    if vis[u]:
        if u == 1:
            print("Yes" if all(vis[1:n+1]) else "No")
        else:
            print("No")
        exit()
    vis[u] = True
    for v in adj[u]:
        if v != parent: # DFS to one direction
            DFS(v, u)

DFS(1, -1)
print("Yes" if all(vis[1:n+1]) else "No")


# OR alternatively
import sys
sys.setrecursionlimit(2 * 10**5 + 5) # IM - must have, to terminate DFS

n, m = map(int, input().split())
if m != n:
    print("No")
    exit()
    
adj = [[] for _ in range(n+1)]
vis = [False] * (n+1)

def DFS(u):
    vis[u] = True
    for v in adj[u]: # dfs both directions
        if not vis[v]:
            DFS(v)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n + 1):
    if len(adj[i]) != 2:
        print("No")
        exit()

DFS(1)
print("Yes" if all(vis[1:n+1]) else "No")