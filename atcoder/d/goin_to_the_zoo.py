import sys
sys.stdin = open("input", "r")


from collections import defaultdict, Counter
n, m = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
k = defaultdict(set)
for animal in range(m):
    _, *zoos = map(int, input().split()) # read definition
    new_zoos = { zoo - 1 for zoo in zoos}
    k[animal] = set(new_zoos)
zoo = defaultdict(set)
for animal, zoos in k.items():
    for z in zoos:
        zoo[z].add(animal)
count = [0]
cnt = {animal: 0 for animal in range(m)}
ans = [float('inf')]
def dfs(pos, sum):
    count[0] += 1
    #print(f"now at pos {pos}, sum is {sum}")
    #print(f"cnt is {cnt}")
    if pos == n:
        if all(c >= 2 for c in cnt.values()):
            ans[0] = min(ans[0], sum)
        return
    
    dfs(pos+1, sum)

    for animal in zoo[pos]:
        cnt[animal] += 1
    dfs(pos+1, sum+c[pos])
    for animal in zoo[pos]:
        cnt[animal] += 1
    dfs(pos+1, sum+c[pos]*2)

    for animal in zoo[pos]:
        cnt[animal] -= 2
dfs(0,0)
print(ans[0])
print(f"count is {count[0]}")



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