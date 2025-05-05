import sys
sys.stdin = open("input", "r")


from collections import defaultdict, Counter
n, m = [int(i) for i in input().split()] # n zoos; m animals
c = [int(i) for i in input().split()] # c is cost for each zoo
k = defaultdict(set)
for animal in range(m):
    _, *zoos = map(int, input().split()) # read problem carefully, need to skip first
    new_zoos = { zoo - 1 for zoo in zoos}
    k[animal] = set(new_zoos) # k are the zoos that contain this animal
zoo = defaultdict(set)
for animal, zoos in k.items():
    for z in zoos:
        zoo[z].add(animal)
count = [0]
cnt = {animal: 0 for animal in range(m)}
ans = [float('inf')]

# IM choice of algo: It needs to find minimum visits with different strategies,
# so it needs to know when to stop "dig deeper" -> Thus choose DFS
# Not BFS: because not just the first minimum visit,
#          need to calc cost, so need to find all possible visits.
def dfs(pos, sum):
    count[0] += 1
    if pos == n:
        # IM - don't use top down to decrease numbers from 2
        # use bottom up counting to see if all are > 2
        if all(c >= 2 for c in cnt.values()):
            ans[0] = min(ans[0], sum)
        return
    
    dfs(pos+1, sum) # do not visit the current one

    for animal in zoo[pos]: # visit the current pos zoo
        cnt[animal] += 1
    dfs(pos+1, sum+c[pos])

    for animal in zoo[pos]: # visit the current pos again
        cnt[animal] += 1
    dfs(pos+1, sum+c[pos]*2)

    for animal in zoo[pos]: # backtrack
        cnt[animal] -= 2
dfs(0,0)
print(ans[0])
print(f"count is {count[0]}")


'''
IM - Don't use below algo. Time limited Exceeded.
It first generate all possible selections (all subsets of combos)
Then it iterates all, although it skips all super-sets, 
but still need to check super-sets unnecessarily, which is not efficient.
Use DFS instead, so it stops "drilling" when reach a solution. 
'''
from itertools import chain, combinations
max_list = []
for i in range(n):
    max_list.extend([i, i])
combos = list(chain.from_iterable(combinations(max_list, r) for r in range(2, len(max_list)+1)))

cost = []
success = []
for combo in combos:
    if (any(Counter(suc) <= Counter(combo) for suc in success)):
        continue
    counts = {animal: 2 for animal in range(m)}
    for z in combo:
        for animal in zoo[z]:
            counts[animal] -= 1 if counts[animal] > 0 else 0
    if all(counts[a] == 0 for a in counts):
        cost.append(sum(c[z] for z in combo))
        success.append(combo)
print(min(cost))