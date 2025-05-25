import sys
sys.stdin = open("input", "r")

N = int(input())
arr = list(map(int, input().split()))

from collections import deque


for k in range(1, N + 1):
    dq = deque()
    window_sum = 0
    for i in range(N):
        while dq and dq[-1][0] <= arr[i]:
            dq.pop()
        dq.append((arr[i], i))
        if dq[0][1] <= i - k:
            dq.popleft()
        if i >= k - 1:
            window_sum += dq[0][0]
    print(window_sum)

