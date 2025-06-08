import sys
sys.setrecursionlimit(1 << 25)
sys.stdin = open("input", "r")

# method 1: dfs traversal from leaves to center
N = int(input())
x = list(map(int, input().split()))

from collections import defaultdict
tree = defaultdict(list)

for _ in range(N - 1):
    u, v, w = [int(i) for i in input().split()]
    u = u - 1 # 0-index
    v = v - 1
    tree[u].append((v, w)) # bidirectional edges
    tree[v].append((u, w))

visited = [False] * N
total_cost = 0

def dfs(u):
    global total_cost
    visited[u] = True
    net = x[u]

    for v, w in tree[u]:
        if not visited[v]:
            # for any edge (u, v, w), eventually |subtree_net_x| will be transferred along it
            # so just sum (the subnet * w)
            sub_net = dfs(v)
            total_cost += abs(sub_net) * w
            net += sub_net

    return net

dfs(0)
print(total_cost)


# method 2: post-order travesal from leaves to center:
total_cost = 0
visited = [False] * N

# for any edge (u, v, w), eventually |subtree_net_x| will be transferred along it
# so just sum (the subnet * w)
# thus the procedure is to move from all leaves to their parent
# IM: therefore, use post-order to handle child-first processing
post_order = []
stack = [(0, -1, 0)] # (node, parent, state): state 0=enter, 1=exit
while stack:
    u, p, w = stack.pop()
    visited[u] = True
    post_order.append((u, p, w)) # exit state
    for v, w in tree[u]:
        if not visited[v]:
            stack.append((v, u, w)) # enter state
 
while post_order:
    u, v, w = post_order.pop()
    total_cost += w * abs(x[u])
    x[v] += x[u]


print(total_cost)