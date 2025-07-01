import sys
sys.stdin = open("input", "r")

import bisect
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    first = arr[0]
    last = arr[-1]
    remain = sorted(arr[1:-1]) # IM: remove end by using -1 (exclusive index)
    valid = last <= 2 * first
    while not valid and remain:
        # find the index that's strictly larger
        idx = bisect.bisect_right(remain, first*2)
        if idx == 0: #IM check out of bound
            break
        first = remain.pop(idx-1) # update the starting point and repeat
        valid = last <= 2*first 
    if valid:
        print(len(arr) - len(remain))
        continue
    print(-1)