import sys
sys.stdin = open("input", "r")

n = int(input())

arrs = []
for _ in range(n):
    arrs.append(input())

catstr = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        catstr.add(arrs[i] + arrs[j])
print(len(catstr))
