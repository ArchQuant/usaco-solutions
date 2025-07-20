import sys
sys.stdin = open("input", "r")

n, k = map(int, input().split())
days = list(map(int, input().split()))

prev = days[0]
cost = k + 1

for curr in days:
    # IM: next gap <= the initial fee
	if curr - prev <= k:
		cost += curr - prev
	else:
		# start a new subscription
		cost += k + 1
	prev = curr

print(cost)