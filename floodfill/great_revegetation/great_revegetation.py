import sys
from collections import deque

sys.stdin = open("input", "r")

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    type_, u, v = input().split()
    u, v = int(u) - 1, int(v) - 1
    same = (type_ == 'S')
    adj[u].append((v, same))
    adj[v].append((u, same))

component_num = 0
impossible = False
color = [-1] * n  # -1 means unvisited

# IM: imagine the picture of a simple component, swap the two type of grass is still valid
# then the problem reduced to "count how many connected components"
# IM: note that this could be  impossible
for i in range(n):
    if color[i] == -1:
        component_num += 1
        queue = deque()
        queue.append((i, True))  # (node, color)

        # find the connected ones
        while queue and not impossible:
            node, c = queue.popleft()
            color[node] = c

            for neighbor, same in adj[node]:
                expected_color = c if same else not c
                if color[neighbor] == -1:
                    queue.append((neighbor, expected_color))
                elif color[neighbor] != expected_color: # cannot satisfy
                    impossible = True
                    break

if impossible:
    print("0")
else:
    print("1" + "0" * component_num)
