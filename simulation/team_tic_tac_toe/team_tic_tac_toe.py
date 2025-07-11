WIDTH = 3

def configs(board, row_cols):
	sets = set()
	for row_col in row_cols:
		r, c = row_col
		sets.add(board[r][c])
	return sets

import sys
sys.stdin = open("input","r")
board = [input() for _ in range(WIDTH)]

# winners[1] is all winning teams with 1 unique cow
# winners[2] is all winning teams with 2 unique cows
winners = [set() for _ in range(WIDTH + 1)]
# IM: Key function which adds a winning team to the winners array
insert = lambda c: winners[len(c)].add(tuple(sorted(c)))

# all rows
for r in range(WIDTH):
	insert(configs(board, [(r, c) for c in range(WIDTH)]))

# all columns
for c in range(WIDTH):
	insert(configs(board, [(r, c) for r in range(WIDTH)])) # both are (r, c)

# diagonals
insert(configs(board, [(i, i) for i in range(WIDTH)]))
insert(configs(board, [(i, WIDTH - i - 1) for i in range(WIDTH)]))

print(len(winners[1]))
print(len(winners[2]))