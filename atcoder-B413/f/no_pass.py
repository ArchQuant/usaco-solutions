import sys
sys.stdin = open("input", "r")


from collections import deque

INF = 10**18

H, W, K = map(int, input().split())
goals = set(tuple(map(int, input().split())) for _ in range(K))

dp = [[[INF]*5 for _ in range(W)] for _ in range(H)]
deg = [[[3]*5 for _ in range(W)] for _ in range(H)]
q = deque()

# Init goal states
for (r, c) in goals:
    i, j = r-1, c-1
    for a in range(1,5):
        dp[i][j][a] = 0
        q.append( (i, j, a) )

# Helper to get neighbor based on b
def move(i,j,b):
    if b == 1 and i>0: return (i-1,j)
    if b == 2 and i+1<H: return (i+1,j)
    if b == 3 and j>0: return (i,j-1)
    if b == 4 and j+1<W: return (i,j+1)
    return (i,j)

while q:
    i,j,a = q.popleft()
    d = dp[i][j][a]
    for b in [1,2,3,4]:
        if b == a: continue
        # seeking predecessors where Takahashi used b to reach (i,j,b)
        # that predecessor is at (pi,pj) with current a_prev = b
        # find all (pi,pj) such that move(pi,pj,b) == (i,j)
        # Equivalently, apply reverse move:
        if b == 1: pi, pj = i+1, j
        if b == 2: pi, pj = i-1, j
        if b == 3: pi, pj = i, j+1
        if b == 4: pi, pj = i, j-1
        if not (0 <= pi < H and 0 <= pj < W):
            pi, pj = pi, pj  # out of bounds => stayed? Actually no, stay only if move invalid, so skip
            continue
        a_prev = b
        if dp[pi][pj][a_prev] != INF:
            continue
        deg[pi][pj][a_prev] -= 1
        best = INF
        # check all b' ≠ a_prev for potential dp
        for b2 in [1,2,3,4]:
            if b2 == a_prev: continue
            ni, nj = move(pi, pj, b2)
            best = min(best, 1 + dp[ni][nj][b2])
        if deg[pi][pj][a_prev] == 0:
            dp[pi][pj][a_prev] = best
            q.append( (pi, pj, a_prev) )

ans = 0
for i in range(H):
    for j in range(W):
        mn = min(dp[i][j][1:])
        if mn < INF:
            ans += mn
print(ans)
