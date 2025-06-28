import sys
sys.stdin = open("input", "r")

n = int(input())
shuffle = [int(i) - 1 for i in input().split()]
cows = list(map(int, input().split()))

# moving backward to find initial order
for _ in range(3):
	past_order = [0] * n
	for i in range(n):
        # reverse assign, instead of cows[shuffle[i]] = ...
		past_order[i] = cows[shuffle[i]]
	cows = past_order.copy()

for i in past_order:
    print(i)