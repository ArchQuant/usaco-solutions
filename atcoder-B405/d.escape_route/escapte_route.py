import sys
sys.stdin = open("input", "r")

h, w = [int(i) for i in input().split()]
s = [ [None] * w for _ in range(h)]

for i in range(h):
    s[i] = list(input())

from collections import deque
q = deque()
for i in range(h):
    for j in range(w):
        if s[i][j] == 'E':
            q.append((i, j))

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    for _ in range(len(q)):
        i, j = q.popleft()
        for di, dj in direct:
            newi, newj = i+di, j+dj
            if 0<=newi<h and 0<=newj<w and s[newi][newj]=='.':
                if di == -1 and dj == 0:
                    s[newi][newj] = 'v'
                elif di == 1 and dj == 0:
                    s[newi][newj] = '^'
                elif di == 0 and dj == -1:
                    s[newi][newj] = '>'
                else:
                    s[newi][newj] = '<'
                q.append((newi, newj))
for row in s:
    print(''.join(row))
            

