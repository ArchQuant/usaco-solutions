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

# IM: checkout method2 below!!

# method1: use dfs to find all subsets of ac choices
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


# method2: bitmask
from typing import NamedTuple

MAX_STALL = 100
# typing.NamedTuple for immutable data class
class Cow(NamedTuple):
	start: int
	end: int
	cool_req: int

class AC(NamedTuple):
	start: int
	end: int
	cool_amt: int
	cost: int

cow_num, ac_num = [int(i) for i in input().split()]
# IM: use NamedTuple for cleanness
cows = [Cow(*[int(i) for i in input().split()]) for _ in range(cow_num)]
acs = [AC(*[int(i) for i in input().split()]) for _ in range(ac_num)]

min_cost = float("inf")
# IM: bitmask iterates over all possible ac scenarios, instead of dfs
for mask in range(1 << ac_num):
	stalls = [0 for _ in range(MAX_STALL + 1)]

	cost = 0
	for v, a in enumerate(acs):
		if mask & (1 << v):
			for i in range(a.start, a.end + 1):
				stalls[i] += a.cool_amt # accumulate all cool_amt
			cost += a.cost

	valid = True
	for c in cows:
		for i in range(c.start, c.end + 1):
			if stalls[i] < c.cool_req: # check each disjoint c
				valid = False
				break
		if not valid:
			break
	else:
		min_cost = min(min_cost, cost)

print(min_cost)