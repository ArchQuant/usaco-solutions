import sys
sys.stdin = open("input", "r")

N = int(input())
elsie = [int(input()) for i in range(N)]
set_elsie = set(elsie) # use set for fast "in"
bessie = [i for i in range(1, 2 * N + 1) if i not in set_elsie] # IM get bessies

# IM: sort, for easy execution of strategy
# IM: high-half: reverse sort, max first, for easy compare
elsie_high = sorted(elsie[: N // 2], reverse=True)
elsie_low = sorted(elsie[N // 2 :])
# now bessie is sorted low to high
bessie_high = sorted(bessie[N // 2 :], reverse=True)
bessie_low = sorted(bessie[: N // 2])
wins, j = 0, 0

# first half - high card: 
# IM: two pointers, i: elsie; j: bessie
# if bessie highest > elsie highest: bessie wins, i++, j++
# else: i++
for i in range(N // 2):
	# if bessie's card > elsie's card, move 
	# then go to next bessie card and elsie card, otherwise bessie can use her worst
	if bessie_high[j] > elsie_high[i]:
		wins += 1
		j += 1

# reversed logic for low card
j = 0
for i in range(N // 2):
	# if bessie lowest < elsie lowest; bessie win, i++, j++
	# otherwise bessie can use her worst
	if bessie_low[j] < elsie_low[i]:
		wins += 1
		j += 1

print(wins)