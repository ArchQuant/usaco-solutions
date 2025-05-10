import sys
sys.stdin = open("input", "r")

n = int(input())
arr = [int(a) for a in input().split()]

ret = 0
# use suffix sum for efficiency
suffix_sum = [0] * (n+1)
for i in range(n-1, -1, -1):
    suffix_sum[i] = suffix_sum[i+1] + arr[i]
for i in range(n):
    ret += arr[i] * suffix_sum[i+1]
print(ret) 