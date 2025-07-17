import sys
sys.stdin = open("input", "r")

n = int(input())
steps = []
for _ in range(n):
    dir_, num_steps = map(str, input().split())
    steps.append((dir_, int(num_steps)))

curr = (0, 0)
# IM: instead of a grid (many unused cells, too coarse),
# use a map {coordinate : time} to track a visited event
visits = {curr: 0}

time = 0
max_regrow = float("inf") # later will use min, so start with +inf
for dir_, num_steps in steps:
	if dir_ == "N":
		delta = 0, 1
	elif dir_ == "W":
		delta = -1, 0
	elif dir_ == "E":
		delta = 1, 0
	elif dir_ == "S":
		delta = 0, -1

	for _ in range(int(num_steps)):
		curr = (curr[0] + delta[0], curr[1] + delta[1])
		time += 1

		# use the map to keep track of past visits
		if curr in visits:
			max_regrow = min(max_regrow, time - visits[curr])
		visits[curr] = time

# Output -1 if FJ has never gone back to the same patch of grass.
output = -1 if max_regrow == float("inf") else max_regrow
print(output)