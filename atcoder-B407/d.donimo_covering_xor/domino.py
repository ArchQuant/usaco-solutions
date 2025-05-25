
import sys
sys.stdin = open("input", "r")

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# all possible ways of placing any number of dominos
# start with empty grid, represented as 0
all_patterns = [0]

# a piece of domino
domino_vertical = (1 << W) + 1  # Vertical: two bits apart by W
domino_horizontal = 3           # Horizontal domino pattern (covers 2 bits)

# For each cell, try to place a domino: to the right or down direction
# Do this for all possible domino placements in an accumulative manner
bit = 0 # each cell position is marked by bit = W * i + j
for i in range(H):
    for j in range(W):
        tmp = []
        for b in all_patterns:
            # domino_horizon is b(11). Use "<< bit" to move bit position
            if j + 1 < W and not (b & (domino_horizontal << bit)):
                tmp.append(b | (domino_horizontal << bit)) # add a domino
            # Check if a vertical domino can be placed
            if i + 1 < H and not (b & (domino_vertical << bit)):
                tmp.append(b | (domino_vertical << bit))
        # Update all_patterns with new placements
        all_patterns.extend(tmp)
        bit += 1

# Compute maximum XOR of uncovered cells
ans = 0
for b in all_patterns:
    now = 0
    bit = 0
    for i in range(H):
        for j in range(W):
            if (1 & ~b >> bit):  # find uncovered cell
                now ^= A[i][j]   # XOR each cell
            bit += 1
    ans = max(ans, now)

print(ans)

'''

import numpy as np


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

N = H * W
grid = np.array(A).flatten()

def get_index(i, j):
    return i * W + j

def in_bounds(i, j):
    return 0 <= i < H and 0 <= j < W

# Compute maximum XOR using DP
# Try all possible domino placements using bitmask DP
# State: (pos, used) where pos is current cell, used is a bitmask of covered cells
dp = {}

def rec(pos, used):
    if pos == N:
        # Compute XOR of uncovered cells
        score = 0
        for i in range(N):
            if not (used & (1 << i)): # check if it is used
                score ^= grid[i]
        return score
    
    if (pos, used) in dp:
        return dp[(pos, used)]
    
    # Skip current cell (leave it uncovered)
    best = rec(pos + 1, used)
    
    # Current cell coordinates
    i, j = divmod(pos, W)
    
    # Try placing a horizontal domino: (i, j) and (i, j+1)
    if j + 1 < W:
        next_pos = get_index(i, j + 1)
        if not (used & (1 << pos)) and not (used & (1 << next_pos)):
            new_used = used | (1 << pos) | (1 << next_pos)
            best = max(best, rec(pos + 2, new_used))
    
    # Try placing a vertical domino: (i, j) and (i+1, j)
    if i + 1 < H:
        next_pos = get_index(i + 1, j)
        if not (used & (1 << pos)) and not (used & (1 << next_pos)):
            new_used = used | (1 << pos) | (1 << next_pos)
            # Skip to next uncovered position
            next_pos_to_try = pos + 1
            while next_pos_to_try < N and (used | (1 << pos) | (1 << next_pos)) & (1 << next_pos_to_try):
                next_pos_to_try += 1
            best = max(best, rec(next_pos_to_try, new_used))
    
    dp[(pos, used)] = best
    return best

print(rec(0, 0))
'''