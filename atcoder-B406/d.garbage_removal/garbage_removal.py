import sys
sys.stdin = open("input", "r")

H, W, N = map(int, input().split())

A = [[] for _ in range(H)]
B = [[] for _ in range(W)]
X = [0] * N
Y = [0] * N
seen = [0] * N  # 0 for unseen, 1 for seen

# instead of using the 2-D grid (waste a lot of space due to sparse matrix)
# we use two 1D arrays X & Y to only store the coordinate that are filled
# then pre-compute A & B where A[i] keeps the "filled coordinate" of i-th row
# Also use seen to keep track of duplicate removal
for i in range(N):
    X[i], Y[i] = map(int, input().split())
    X[i] -= 1  # 0-index
    Y[i] -= 1
    A[X[i]].append(i)
    B[Y[i]].append(i)

Q = int(input())
for _ in range(Q):
    t, a = map(int, input().split())
    a -= 1  # 0-index
    ans = 0
    if t == 1:
        while A[a]:
            idx = A[a].pop()
            ans += 1 - seen[idx]
            seen[idx] = 1
    else:  # Process column a
        while B[a]:
            idx = B[a].pop()
            ans += 1 - seen[idx]
            seen[idx] = 1
    
    print(ans)


'''
h, w, n = [int(i) for i in input().split()]
grid = [[0] * w for _ in range(h)]
for _ in range(n):
    x, y = [int(i) for i in input().split()]
    grid[x-1][y-1] = 1

q = int(input())
for _ in range(q):
    qt, k = [int(i) for i in input().split()]
    if qt == 1:
        print(sum(grid[k-1]))
        for c in range(w):
            grid[k-1][c] = 0
    elif qt == 2:
        ret = 0
        for r in range(h):
            ret += grid[r][k-1]
            grid[r][k-1] = 0
        print(ret)
'''
