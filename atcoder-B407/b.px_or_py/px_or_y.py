import sys
sys.stdin = open("input", "r")

x, y = [int(i) for i in input().split()]

comb = []
for i in range(1,7):
    for j in range(1,7):
        comb.append((i,j))

count = 0
for a, b in comb:
    if a + b >= x or abs(a - b) >= y:
        count += 1
print(count/len(comb))