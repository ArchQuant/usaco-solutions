import sys
sys.stdin = open("input", "r")

from collections import deque
qs = deque()
N = int(input())
for _ in range(N):
    q = [int(i) for i in input().split()]
    match q:
        case [1, c, x]:
            qs.append((c, x))
        case [2, k]:
            ret = 0
            while k > 0:
                cur = qs.popleft()
                if cur[0] > k:
                    qs.appendleft((cur[0] - k, cur[1]))
                    ret += k * cur[1]
                    k = 0
                else:
                    k -= cur[0]
                    ret += cur[0] * cur[1]
            print(ret)