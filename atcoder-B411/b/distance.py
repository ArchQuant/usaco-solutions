import sys
sys.stdin = open("input", "r")

n = int(input())
arr = [int(i) for i in input().split()]

from itertools import accumulate
cum_sum = list(accumulate(arr, initial=0))

for i in range(n-1):
    for j in range(i+1, n):
        print(cum_sum[j]-cum_sum[i], end=" ")
    print("")


