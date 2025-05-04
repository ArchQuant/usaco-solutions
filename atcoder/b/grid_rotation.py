import sys
sys.stdin = open("input", "r")

n = int(input())

s = [[None] * n for _ in range(n)]
t = [[None] * n for _ in range(n)]

for i in range(n):
    s[i] = list(input())
for i in range(n):
    t[i] = list(input())

s_rot = [s] # IM
all_counts = []
for k in range(1, 4): # IM
    s_rot.append([[s_rot[k-1][n-1-j][i] for j in range(n)] for i in range(n)]) # IM
for k in range(len(s_rot)):
    op_count = k
    for i in range(n):
        for j in range(n):
            if s_rot[k][i][j] != t[i][j]:
                op_count += 1
    all_counts.append(op_count)

print(min(all_counts))

'''
op_count = 0

from collections import deque
q = deque([s])
visited = set()

switch = {'.':'#', '#': '.'}
op = 0
flat_t = ''.join(c for row in t for c in row)
while q:
    op += 1
    for _ in range(len(q)):
        curr_s = q.popleft()
        for i in range(n):
            for j in range(n):
                new_s_chg = [row[:] for row in curr_s] # IM
                new_s_chg[i][j] = switch[new_s_chg[i][j]]
                flat_s = ''.join(c for row in new_s_chg for c in row) # IM
                if flat_s == flat_t:
                    print(op)
                    exit()
                if flat_s not in visited:
                    visited.add(flat_s)
                    q.append(new_s_chg)
        new_s_rot = [[curr_s[n-1-j][i] for j in range(n)] for i in range(n)] # IM


        flat_s = ''.join(c for row in new_s_rot for c in row)
        if flat_s == flat_t:
            print(op)
            exit()
        if flat_s not in visited:
            visited.add(flat_s)
            q.append(new_s_rot)

''' 