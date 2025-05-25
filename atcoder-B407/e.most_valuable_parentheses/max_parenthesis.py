
import sys
sys.stdin = open("input", "r")

import heapq

# Algo: each iteration, add the next two element, then select the largest one so far
# Eventually, there will be half chosen, and the result is the max
def solve(n: int, a: list[int]) -> int:
    ans = 0
    que = []  # min-heap used as a max heap
    for i in range(n):
        if i == 0:
            heapq.heappush(que, -a[i * 2])  # first one must be '('
        else:
            heapq.heappush(que, -a[i * 2 - 1])  # 1, 3, 5...
            heapq.heappush(que, -a[i * 2])      # 2, 4, 6...
        v = -heapq.heappop(que)  # Get the max value
        ans += v # greedy algo: every time should be the largest one so far
    return ans

T = int(input())
for _ in range(T):
    n = int(input())
    a = [int(input()) for _ in range(2*n)]
    print(solve(n, a))