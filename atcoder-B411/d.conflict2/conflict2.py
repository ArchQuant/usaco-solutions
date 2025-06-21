import sys
sys.stdin = open("input", "r")

n, m = [int(i) for i in input().split()]
op, p, s = [], [], []

for _ in range(m):
    parts = input().split()
    op.append(int(parts[0]))
    p.append(int(parts[1]))
    if parts[0] == '2':
        reversed_s = parts[2][::-1]
        s.append(reversed_s)
    else:
        s.append("")

# Index: for simplicity, server index = 0; all other PCs use 1-index
ans = ""
i = 0 # i tracks the changes
# IM: Reverse scan, think DP, reduce branching.
# By reversing each process:
# 1 p: replace s[p] with s[0] -> set i=0, so that when keep reverse scanning, only query on 0 will be triggered (type 3)
# 2 p s: s[p] += s -> updating ans, only queries on p will be triggered
# 3 p: replace s[0] with s[p] -> set i=p, so that when keep reverse scanning, only the queries on p will be triggered
for t in reversed(range(m)):
    if op[t] == 1:
        if p[t] == i:
            i = 0
    elif op[t] == 2:
        if p[t] == i:
            ans += s[t]
    else:
        if i == 0:
            i = p[t]

print(ans[::-1])



"""
#ETL
queries = []
for i in range(m):
    q = input().split()
    queries.append(q)
    match q:
        case ["1", p]:
            p = int(p) - 1
            pcs[p] = server.copy()
        case ["2", p, _]:
            p = int(p) - 1
            pcs[p] += [i]
        case ["3", p]:
            p = int(p) - 1
            server = pcs[p].copy()
output = ""
for j in server:
    output += queries[j][2]
print(output)
"""


"""
# ETL
for _ in range(m):
    q = input().split()
    match q:
        case ["1", p]:
            p = int(p) - 1
            pcs[p] = server
        case ["2", p, s]:
            p = int(p) - 1
            pcs[p] += s
        case ["3", p]:
            p = int(p) - 1
            server = pcs[p]
print(server)
"""