import sys
sys.stdin = open("input", "r")

n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]

def rotate_clockwise(board):
    # IM- [::-1] reverse all rows from row[-1] -> row[0]
    # then take the first element of each
    return [list(row) for row in zip(*board[::-1])]

min_op = float('inf')
for k in range(4): # IM - keep track of rotation times
    op_count = k
    # IM - use sum for clarity
    op_count += sum(1 for i in range(n) for j in range(n) if s[i][j] != t[i][j])
    min_op = min(min_op, op_count)
    # IM - two types of op, only change s for rotation, don't switch char
    s = rotate_clockwise(s)
print(min_op)

'''
# More verbose version:
s_rot = [s] # IM - zero rotation -> original s
all_counts = []

# IM - the two loops below are both 4, so can combine
for k in range(1, 4): # IM - skip the initial one
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
'''
IM - Don't use BFS for this case.
Because (rotation + change char) are not equivalent operations.
Rotation is at most three times. More rotation will just repeat.


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