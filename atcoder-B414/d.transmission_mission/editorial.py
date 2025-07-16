from typing import List
from itertools import accumulate

import sys
sys.stdin = open("input", "r")
N, M = map(int, input().split())
X = [int(i) for i in input().split()]

X.sort()
# a single segment that covvers all
ret = X[-1] - X[0]

# IM: break in to M segments, by removing the largest (M-1) gaps
# IM: after removing (M-1) gaps, there are M segment in total
diffs = [X[i] - X[i-1] for i in range(1, N)]
diffs.sort()

print(ret - sum(diffs[N-1 -(M-1):]))