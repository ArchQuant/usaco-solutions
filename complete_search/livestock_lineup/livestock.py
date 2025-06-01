import sys
sys.stdin = open("input", "r")

import itertools
# in lexicographical order
NAMES = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
# for simplicity, use a dict to convert str into int
COWS = {name: i for i, name in enumerate(NAMES)}

k = int(input())
rules = []
for _ in range(k):
    raw = input().split()
    rules.append((COWS[raw[0]], COWS[raw[-1]]))

def is_valid(arr):
    for a, b in rules:
        # IM - to express that positions are beside each other, use index
        if abs(arr.index(a) - arr.index(b)) != 1:
            return False
    return True

# IM permutation is already in lexicographical order, so stop at the first hit
for arr in itertools.permutations(range(len(COWS))):
    if is_valid(arr):
        for cow in arr:
            print(NAMES[cow])
        exit()
    