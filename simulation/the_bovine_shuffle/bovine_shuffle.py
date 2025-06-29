import sys
sys.stdin = open("input", "r")

n = int(input())
shuffle = [int(i) - 1 for i in input().split()]
cows = list(map(int, input().split())) # "1234567" is a single ID

# moving backward to find initial order
for _ in range(3):
	prev_order = [0] * n
	for i in range(n):
        # reverse assign, instead of cows[shuffle[i]] = ...
		prev_order[i] = cows[shuffle[i]]
	cows = prev_order.copy()

for i in prev_order:
    print(i)