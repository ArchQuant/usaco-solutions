# IM - find a way to represent each arrangement:
# method 1: permutation: e.g., [6, 0, 5, 1, 4, 3, 7, 2] unique for each row
# method 2: backtrack to add one column at a time

import sys
sys.stdin = open("input","r")

# method 1
import itertools
N = 8
grid = [list(input().strip()) for _ in range(N)]
# use a T/F grid for easy check validity
blocked = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        blocked[i][j] = grid[i][j] == '*'

def is_valid(arr):
    # use vector instead of set for speed
    diag = [False] * (2 * N)
    anti_diag = [False] * (2 * N)
    for r in range(len(arr)):
        c = arr[r]
        if blocked[r][c]:
            return False
        if diag[r - c + N]:
            return False
        else:
            diag[r - c + N] = True
        if anti_diag[r + c]:
            return False
        else:
            anti_diag[r + c] = True
    return True

count_valid = 0
for arr in itertools.permutations(range(N)):
    if is_valid(arr):
        count_valid += 1

print(count_valid)

# method 2
N = 8

rows_taken = [False] * N
diag = [False] * (N * 2 - 1)
anti_diag = [False] * (N * 2 - 1)

valid_num = 0
# add one column at a time
def search_queens(c: int = 0):
    # IM: use global in recursive func
	global valid_num
	if c == N:
		valid_num += 1
		return

	for r in range(N):
		row_open = not rows_taken[r]
		diag_open = not anti_diag[r + c] and not diag[r - c + N - 1]
		if not blocked[r][c] and row_open and diag_open:
			# A row and two diagonals have been taken
			rows_taken[r] = anti_diag[r + c] = diag[r - c + N - 1] = True
			search_queens(c + 1)
			# And now they aren't anymore
			rows_taken[r] = anti_diag[r + c] = diag[r - c + N - 1] = False


search_queens()
print(valid_num)
