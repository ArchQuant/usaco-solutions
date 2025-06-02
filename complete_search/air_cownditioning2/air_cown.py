import sys
sys.stdin = open("input", "r")

import itertools

BARN = 100
n, m = [int(i) for i in input().split()]
cows = []
for _ in range(n):
    s, t, c = [int(i) for i in input().split()]
    cows.append((s, t, c))
ac = []
for _ in range(m):
    a, b, p, c = [int(i) for i in input().split()]
    ac.append((a, b, p, c))

# IM: use dfs to find all subsets of ac choices
# ac is numbered [0, 1, 2, ..., m], dfs generates all subsets of ac
def dfs(i, cur, arr, arrs):
    if i == m:
        arrs.append(cur)
        return
    dfs(i+1, cur, arr, arrs)
    dfs(i+1, cur+[arr[i]], arr, arrs)

arrs = []
dfs(0, [], list(range(m)), arrs)

# IM: use cumsum to find temperature requirements
stalls = [0] * (BARN + 1)
for s, t, c in cows:
    stalls[s] = c # all cow slots are disjoint, so use '=' is okay. No need for '+='
    stalls[t+1] = -c

stalls = list(itertools.accumulate(stalls))

def is_valid(arr):
    temp = [0] * (BARN + 1)
    for i_ac in arr:
        a, b, p, _ = ac[i_ac]
        temp[a] += p # IM: cumsum use '+=' instead of '=', due to possible overlap!!
        temp[b+1] += -p
    temp = list(itertools.accumulate(temp))
    if all(t >= s  for t, s in zip(temp, stalls)):
        return True
    else:
        return False

min_cost = float('inf')
# iterate all possible ac choices
for arr in arrs:
    if is_valid(arr):
        cost = sum(ac[i][3] for i in arr)
        min_cost = min(min_cost, cost)

print(min_cost)
